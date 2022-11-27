
import requests
from easygui import enterbox

kyword = enterbox("Enter GSTIN","GSTIN")

requrl = 'https://blog-backend.mastersindia.co/api/v1/custom/search/einvoice_status/'
params = {"keyword":kyword}
apirsp = requests.get("GET",requrl,params=params)
print(apirsp.json())
