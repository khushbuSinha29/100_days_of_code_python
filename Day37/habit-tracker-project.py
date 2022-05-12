# Here we are using Pixela API
# use of API POST, PUT, DELETE and HEADER

import requests
from datetime import datetime

# creating a user

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME= "user name"
TOKEN = "enter your token"
GRAPH_ID = 'graph id'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor':'yes',
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# ****************************************************************
# creating a graph

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    'id': GRAPH_ID,
    'name': 'Cycling Graph',
    'unit': 'Km',
    'type': 'float',
    'color': 'shibafu'
}
headers = {
    'X-USER-TOKEN': TOKEN
}
# response = requests.post(url= graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# *********************************
# creating a pixel

today = datetime(year=2022, month=5, day=11)
date = today.strftime('%Y%m%d')


pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_update = {
    'date': today.strftime('%Y%m%d'),
    'quantity': '5',
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_update, headers=headers)
# print(response.text)

# *****************************************
# updating the value of pixel

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"

pixel_update_data = {
    'quantity': '13'
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_update_data, headers=headers)
# print(response.text)

# ******************************************************
# Deleting the pixel

pixel_delete_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}'
response = requests.delete(url=pixel_delete_endpoint, headers = headers)
print(response.text)