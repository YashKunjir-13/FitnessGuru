from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  

DB_HOST = "localhost"
DB_NAME = "ptdb"  
DB_USER = "postgres"          
DB_PASS = "newpassword"          

UPLOAD_FOLDER = 'static/uploads'  
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

def check_user_exists(username):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM pt_tab WHERE username = %s", (username,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return user


@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if username already exists
        if check_user_exists(username):
            flash("User with the same name exists.")
            return redirect(url_for('register'))

        conn = None
        try:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("INSERT INTO pt_tab (username, password) VALUES (%s, %s)", (username, password))
            conn.commit()
            cur.close()
            flash("Successfully registered, login now.")
            return redirect(url_for('signin'))
        except Exception as e:
            flash("Registration failed: " + str(e))  
            return redirect(url_for('register'))
        finally:
            if conn:
                conn.close()

    return render_template('register.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM pt_tab WHERE username = %s AND password = %s", (username, password))
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user:
            return redirect(url_for('main'))  
        else:
            flash("Invalid username or password. Please try again.")  
            return redirect(url_for('signin'))  

    return render_template('signin.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/bmr')
def bmr():
    return render_template('bmr.html') 

@app.route('/track')
def track():
    return render_template('track.html')

if __name__ == '__main__':
    app.run(debug=True)
