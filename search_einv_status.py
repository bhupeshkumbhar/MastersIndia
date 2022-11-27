
import requests
from easygui import enterbox
import pandas as pd

gstin = enterbox("Enter GSTIN","GSTIN")

req_url = 'https://blog-backend.mastersindia.co/api/v1/custom/search/einvoice_status/?keyword='+gstin
response = requests.get(req_url)
print(response.json())
print('\n\n')