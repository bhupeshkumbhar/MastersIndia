
import requests
from easygui import enterbox

kyword= enterbox("Enter HSN Code","HSN Code")

requrl = 'https://blog-backend.mastersindia.co/api/v1/custom/search/hsn_and_rate/'
params = {"keyword":kyword}
apirsp = requests.request("GET",requrl,params=params)
print(apirsp.json())


