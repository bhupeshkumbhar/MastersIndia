from requests.auth import HTTPBasicAuth
import requests
api_url = 'https://easy-authenticator.p.rapidapi.com/verify'
api_qry = {"secretCode":"333K6O6QVP5SH7UR7JH7A6RGT3LZMWZB","token":"628235","name":"bhupesh.kumbhar"}
api_hdr = {"X-Rapidapi-Key":"472f53a83bmsh0945009f2fe0c7bp1d4da4jsn137f40e946b5","X-RapidAPI-Host": "easy-authenticator.p.rapidapi.com"}

response = requests.request("POST",api_url,headers=api_hdr,params=api_qry)
if response.json()["verify"]:
    print("Status : True")
else:
    print("Status : False")