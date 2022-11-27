from requests.auth import HTTPBasicAuth
import requests
from easygui import enterbox

panno = enterbox("Please enter PAN Number")
api_url = 'https://pan-card-verification-at-lowest-price.p.rapidapi.com/verifyPan/'+panno

api_hdr = {"X-Rapidapi-Key":"472f53a83bmsh0945009f2fe0c7bp1d4da4jsn137f40e946b5","X-RapidAPI-Host": "pan-card-verification-at-lowest-price.p.rapidapi.com"}
response = requests.request("GET",api_url,headers=api_hdr)
print(response.json())