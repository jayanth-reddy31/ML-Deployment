# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 19:41:55 2025

@author: USER
"""

import json
import requests


url = 'https://379e-34-148-132-147.ngrok-free.app/diabetes_prediction'


input_data_for_model = {
    'Pregnancies' : 40,
    'Glucose' : 110,
    'BloodPressure' : 92,
    'SkinThickness' : 0,
    'Insulin' : 0,
    'BMI' : 37.6,
    'DiabetesPredigeeFunction' : 0.191,
    'Age' : 30
    }


#convert the dictonary into json

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)

print(response.text)


