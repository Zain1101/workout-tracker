import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
GENDER = os.getenv("GENDER")
WEIGHT_KG = os.getenv("WEIGHT_KG")
HEIGHT_CM = os.getenv("HEIGHT_CM")
AGE = os.getenv("AGE")
sheety_endpoint = os.getenv("SHEETY_ENDPOINT")
sheet_username = os.getenv("SHEETY_USERNAME")
sheet_password = os.getenv("SHEETY_PASSWORD")


exercise_text=input("Tell about your workout:\n")
headers={
    "x-app-id":APP_ID,
    "x-app-key":API_KEY
}
url="https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_params={
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response= requests.post(url=url,json=exercise_params,headers=headers)
response.raise_for_status()
result = response.json()
print(result)

today_date= datetime.now().strftime("%Y%m%d")
now_time = datetime.now().strftime("%X")


for exercise in result['exercises']:
    sheet_inputs={
        "workout": {
            "date":today_date,
            "time":now_time,
            "exercise":exercise['name'].title(),
            'duration':exercise["duration_min"],
            "calories":exercise["nf_calories"]
        }
    }

#Basic Authentication
sheet_response = requests.post(sheety_endpoint,json=sheet_inputs, auth=(sheet_username,sheet_password))
sheet_response.raise_for_status()
