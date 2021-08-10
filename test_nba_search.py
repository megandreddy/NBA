import pytest
import requests
import json
import os
import ast
from dotenv.main import load_dotenv
import http.client
load_dotenv()

API = os.getenv("api_key")

@pytest.fixture(scope="module")
def parsed_response():
    print("MAKING A NETWORK REQUEST...")    
    conn = http.client.HTTPSConnection("api.sportradar.us")
    conn.request("GET", f"/nba/trial/v7/en/teams/583ecae2-fb46-11e1-82cb-f4ce4684ea4c/profile.json?api_key={API}")  
    res_nba_teams = conn.getresponse()
    nba_teams_data = res_nba_teams.read()
    nba_teams_dict_str = nba_teams_data.decode("UTF-8")
    nba_teams_datas = ast.literal_eval(nba_teams_dict_str)
    team_players = nba_teams_datas["players"]
    return json.loads(team_players)
