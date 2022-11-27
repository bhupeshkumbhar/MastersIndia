
import requests
from easygui import enterbox
import pandas as pd

kword = enterbox("Enter Company Name or Pan Number","Name or PAN Number")


req_url = 'https://blog-backend.mastersindia.co/api/v1/custom/search/name_and_pan/?keyword='+kword
response = requests.get(req_url)
print(response.json())
print('\n\n')

