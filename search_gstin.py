
import requests
from easygui import enterbox
import pandas as pd

gstin = enterbox("Enter GSTIN","GSTIN")

req_url = 'https://blog-backend.mastersindia.co/api/v1/custom/search/gstin/?keyword='+gstin+'&unique_id=93845'

response = requests.get(req_url)
outp  = response.json()
xlist = []
xlist.append(outp["data"])
df = pd.DataFrame(xlist)
print(df)


