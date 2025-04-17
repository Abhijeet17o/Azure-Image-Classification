import requests
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

url = os.getenv("AZURE_IMG_ENDPOINT")
headers = {
    "Prediction-Key": os.getenv("AZURE_IMG_PRED_KEY"),
    "Content-Type": "application/octet-stream"
}

with open(r"C:\ALL CODES\ALL PYTHON\AutoML\data\test-cats-dogs\Dog\111.jpg", "rb") as image_data:
    response = requests.post(url, headers=headers, data=image_data)

print(response.json())
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
