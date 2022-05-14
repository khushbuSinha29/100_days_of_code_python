# API'S used - nutritionix for getting the excercise data
#              sheety - which converts the mspreadsheet into restful JSON API. It means you can access you can
# access your spreadsheet data in a standard way using simple url and HTTP requests.

import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
import os

GENDER = "YOUR GENDER"
WEIGHT_KG = "YOUR WEIGHT"
HEIGHT_CM = "YOUR HEIGHT"
AGE =" YOUR AGE"

APP_ID = "Your APP id"
# APP_ID = os.environ["Your APP id"]
API_KEY = "your api key"

sheet_endpoint = "your sheety endpoint"
excercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

excercise_text = input("Which exercise you did?")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    'query': excercise_text,
    'gender':'Female',
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE
}

response = requests.post(excercise_endpoint, json=parameters, headers=headers)
result = response.json()
# print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result['exercises']:
    sheet_inputs = {
        'sheet1': {
            'date': today_date,
            'time': now_time,
            'exercise':exercise['name'],
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }

# #Bearer Token Authentication
bearer_headers = {
    "Authorization": f"Bearer {'your key'}"
}
sheet_response = requests.post(
    sheet_endpoint,
    json=sheet_inputs,
    headers=bearer_headers
)
print(sheet_response.text)

# sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
# print(sheet_response.text)

# basic authentication
# sheet_response = requests.post(
#     sheet_endpoint,
#     json=sheet_inputs,
#     auth=(
#         os.environ['user name'],
#         os.environ[password]
#     )
# )
# sheet_response = requests.get(sheet_endpoint, auth=HTTPBasicAuth(user, password))
# print(sheet_response.text)
