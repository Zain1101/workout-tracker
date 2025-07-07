import requests
from datetime import datetime

APP_ID= "5c82f9e4"
API_KEY="9a9a8ac79dbfc2d3d518585f217d9fd8"
GENDER="male"
WEIGHT_KG="65"
HEIGHT_CM="170"
AGE="20"

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

sheety_endpoint="https://api.sheety.co/8e9d04e95a1d223b72cd70815b818908/myWorkouts2/workouts"

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
sheet_response = requests.post(sheety_endpoint,json=sheet_inputs, auth=("zain1101","shah@5372"))
sheet_response.raise_for_status()
