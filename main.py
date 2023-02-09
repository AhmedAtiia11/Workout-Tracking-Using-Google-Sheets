import requests
import os
from datetime import datetime
#---------------Nutritionix Parameters-------------------#
APP_ID=os.environ.get("APP_ID")
API_KEY=os.environ.get("API_KEY")
TOKKEN=os.environ.get("TOKKEN")
#----------------------END POINTS---------------------#
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint =os.environ.get("sheet_endpoint")


#-----------------HEADERS AND PARAMETERS---------------#

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
sheet_headers={"Authorization": TOKKEN}

exercise_text = input("Tell me which exercises you did: ")
parameters = {
    "query":exercise_text,
    "gender":"male",
    "weight_kg":75,
    "height_cm":191.00,
    "age":23
}

#-------------------RESPONSES-----------------------#
response = requests.post(nutritionix_endpoint, json=parameters, headers=nutritionix_headers)
result = response.json()
# print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response=requests.post(url=sheet_endpoint,headers=sheet_headers,json=sheet_inputs)
    print(sheet_response.json())
