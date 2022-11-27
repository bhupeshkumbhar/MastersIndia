
import requests
from easygui import enterbox
import pandas as pd

kyword = enterbox("Enter GSTIN","GSTIN")

requrl = 'https://blog-backend.mastersindia.co/api/v1/custom/search/gst_return_status/'
params = {"keyword":kyword,"financial_year":"2022-23"}
apirsp = requests.request("GET",requrl,params=params)
output  = apirsp.json()
outlst = output["data"]["EFiledlist"]
dframe = pd.DataFrame(outlst)
print(dframe)


