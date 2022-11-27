
import requests
from easygui import enterbox
import pandas as pd

gstin = enterbox("Enter GSTIN","GSTIN")

req_url = 'https://blog-backend.mastersindia.co/api/v1/custom/search/gst_return_status/?keyword='+gstin+'&financial_year=2022-23'
response = requests.get(req_url)
outp  = response.json()
xlist = outp["data"]["EFiledlist"]
df = pd.DataFrame(xlist)
print(df)


