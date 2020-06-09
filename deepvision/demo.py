#!python3
import requests

modes = ['vehicle','context','face','brand','<SERVICE NAME>']
imagen = "/home/martin/Downloads/Practicas/deepvision/download.jpeg"
token = 'AAAG0tXjVlt9uTQwbvd3W0wAykE%3AGZu9UYjcBafSLk2tifmJ04BJ77E'

r =requests.post("https://api.visualintelligence.deepvisionai.com/predict",data={"vehicle|modes": "detect|view|mmy_us","image": imagen},headers={"api-key": token},)

print(r)

# JSON Response
# Our API returns a JSON file with the list of concepts we recognized and its corresponding probability scores on the likelihood we estimate these concepts are present in your images.

# [
#   {
#     "View": {
#       "score": 0.59,
#       "view": "Cargo Area View"
#     },
#     "license_plate": {},
#     "mmy": {}
#   }
# ]

