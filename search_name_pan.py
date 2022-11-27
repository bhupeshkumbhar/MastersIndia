
import requests
from easygui import enterbox
import pandas as pd

kyword = enterbox("Enter Company Name or Pan Number","Name or PAN Number")
requrl = 'https://blog-backend.mastersindia.co/api/v1/custom/search/name_and_pan/'
params = {"keyword":kyword,"unique_id":394948}
apirsp = requests.request("GET",requrl,params=params)
print(apirsp.json())


