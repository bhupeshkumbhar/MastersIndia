
import requests
from bs4 import BeautifulSoup
import pandas as pd

print('Enter your gstin:')
gstin = input()

req_url = 'https://blog-backend.mastersindia.co/api/v1/custom/search/gstin/?keyword='+gstin+'&unique_id=93845'

response = requests.get(req_url)
outp  = response.json()
xlist = []
xlist.append(outp["data"])
df = pd.DataFrame(xlist)
print(df)


req_url = 'https://blog-backend.mastersindia.co/api/v1/custom/search/gst_return_status/?keyword='+gstin+'&financial_year=2022-23'
response = requests.get(req_url)
outp  = response.json()
print(outp)
xlist = outp["data"]["EFiledlist"]
df = pd.DataFrame(xlist)
print(df)


# req_url = 'https://blog-backend.mastersindia.co/api/v1/custom/search/hsn_and_rate/?keyword=8902'
# response = requests.get(req_url)
# print(response.json())
# print('\n\n')

# req_url = 'https://blog-backend.mastersindia.co/api/v1/custom/search/name_and_pan/?keyword=UMASONS'
# response = requests.get(req_url)
# print(response.json())
# print('\n\n')

# req_url = 'https://blog-backend.mastersindia.co/api/v1/custom/search/einvoice_status/?keyword=27AAACU4276H1Z6'
# response = requests.get(req_url)
# print(response.json())
# print('\n\n')