
import requests
from bs4 import BeautifulSoup
import pandas as pd

req_url = 'https://blog-backend.mastersindia.co/api/v1/custom/search/gstin/?keyword=27AAACU4276H1Z6&unique_id=93845'

response = requests.get(req_url)
print(response.json())
print('\n\n')

req_url = 'https://blog-backend.mastersindia.co/api/v1/custom/search/gst_return_status/?keyword=27AABCZ0417C1ZR&financial_year=2022-23'
response = requests.get(req_url)
print(response.json())
print('\n\n')

req_url = 'https://blog-backend.mastersindia.co/api/v1/custom/search/hsn_and_rate/?keyword=8902'
response = requests.get(req_url)
print(response.json())
print('\n\n')

req_url = 'https://blog-backend.mastersindia.co/api/v1/custom/search/name_and_pan/?keyword=UMASONS'
response = requests.get(req_url)
print(response.json())
print('\n\n')

req_url = 'https://blog-backend.mastersindia.co/api/v1/custom/search/einvoice_status/?keyword=27AAACU4276H1Z6'
response = requests.get(req_url)
print(response.json())
print('\n\n')