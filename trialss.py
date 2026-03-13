import requests

API_KEY = "AIzaSyAjDAFU-0Gek0AyGgootqQ3RVOXeDKL2W4"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"

data = {
    "contents": [
        {
            "parts": [{"text": "What is the capital of India?"}]
        }
    ]
}

headers = {"Content-Type": "application/json"}
response = requests.post(URL, json=data, headers=headers)

print(response.json())  # Output the response



{'candidates': [{'content': {'parts': [{'text': 'New Delhi'}], 'role': 'model'}, 'finishReason': 'STOP', 'index': 0, 'safetyRatings': [{'category': 'HARM_CATEGORY_SEXUALLY_EXPLICIT', 'probability': 'NEGLIGIBLE'}, {'category': 'HARM_CATEGORY_HATE_SPEECH', 'probability': 'NEGLIGIBLE'}, {'category': 'HARM_CATEGORY_HARASSMENT', 'probability': 'NEGLIGIBLE'}, {'category': 'HARM_CATEGORY_DANGEROUS_CONTENT', 'probability': 'NEGLIGIBLE'}]}], 'usageMetadata': {'promptTokenCount': 7, 'candidatesTokenCount': 2, 'totalTokenCount': 9}, 'modelVersion': 'gemini-pro'}