import pytest
import requests
import json
import os
from dotenv.main import load_dotenv
import http.client
load_dotenv()

API = os.getenv("api_key")

@pytest.fixture(scope="module")
def parsed_response():
    print("MAKING A NETWORK REQUEST...")    
    conn = http.client.HTTPSConnection("api.sportradar.us")
    conn.request("GET", f"/nba/trial/v7/en/teams/583ecae2-fb46-11e1-82cb-f4ce4684ea4c/profile.json?api_key={API}")
    #response = requests.get(f"/nba/trial/v7/en/teams/583ecae2-fb46-11e1-82cb-f4ce4684ea4c/profile.json?api_key={API}")
    response = requests.get(conn.request)
    return json.loads(response.text)