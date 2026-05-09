
import requests

url = "http://127.0.0.1:5000/predict"

text = input("Enter text for sentiment analysis: ")

response = requests.post(url, json={"text": text})

print("Prediction Result:")
print(response.json())
