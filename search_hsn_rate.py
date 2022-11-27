
import requests
from easygui import enterbox

hsncd = enterbox("Enter HSN Code","HSN Code")

req_url = 'https://blog-backend.mastersindia.co/api/v1/custom/search/hsn_and_rate/?keyword='+hsncd
response = requests.get(req_url)
print(response.json())
print('\n\n')

