import requests
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

url = os.getenv("AZURE_URL_ENDPOINT")
headers = {
    "Prediction-Key": os.getenv("AZURE_IMG_URL_PRED_KEY"),
    "Content-Type": "application/json"
}
data = {
    "Url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQApg95yTjHqvgWzOPIoxGZ_XZv1UsNLzwZ7uDUPT5vXkrlAYC3YaD65O_Dlm8UY3aTtCg&usqp=CAU"
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
