import json
import re
import statistics
import requests

print("-------------------------")
x = input("Do you want to find the best player for your team? (Type Yes or No):")


import json
import requests
import os
from dotenv import dotenv_values
from dotenv.main import load_dotenv
load_dotenv()

api = os.getenv("api_key")
#url = 'https://api.sportradar.us/nba/{access_level}/{version}/{language_code}/league/free_agents.{format}?api_key={your_api_key}'
#final_url = f'{url}'


#url = "https://api.sportradar.us/nba/trial/v7/en/league/free_agents.json?"
#final_url = f'{url}api_key={api}'

import http.client

conn = http.client.HTTPSConnection("api.sportradar.us")

conn.request("GET", "/nba/trial/v7/en/league/free_agents.json?api_key=zcbqec5qr9v7w7s59rcfmvqm")

res = conn.getresponse()
data = res.read()

print(data)

print("Now, what position are you looking for? (Input PG, SG, SF, PF, or C):")
