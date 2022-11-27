
import requests
from easygui import enterbox
import pandas as pd

kyword= enterbox("Enter GSTIN","GSTIN")
requrl = 'https://blog-backend.mastersindia.co/api/v1/custom/search/gstin/'
params = {"keyword":kyword,"unique_id":394948}
apirsp = requests.request("GET",requrl,params=params)
output  = apirsp.json()
rsplst = []
rsplst.append(output["data"])
dframe = pd.DataFrame(rsplst)
print(dframe)


