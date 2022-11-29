from requests.auth import HTTPBasicAuth
import requests
api_url = 'https://easy-authenticator.p.rapidapi.com/newAuthKey?'
api_qry = {"account":"Sandeep.Kulkarni","issuer":"ZENCON"}
api_hdr = {"X-Rapidapi-Key":"472f53a83bmsh0945009f2fe0c7bp1d4da4jsn137f40e946b5","X-RapidAPI-Host": "easy-authenticator.p.rapidapi.com"}

response = requests.request("POST",api_url,headers=api_hdr,params=api_qry)
print(response.json())