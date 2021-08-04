import ast
from logging import NullHandler
import os
import http.client
from dotenv.main import load_dotenv
from pprint import pprint
import re
import csv
load_dotenv()

API = os.getenv("api_key")

print("-------------------------")
x = input("Do you want to find the best player for your team? (Type Yes or No): ")
if x.upper() == "YES":
    print("Great, let's do this. Here's the entire list of available players...")
else:
    print("Alright, well good luck building a championship team without us! Have a good day :-)")
    exit()

conn = http.client.HTTPSConnection("api.sportradar.us")
conn.request("GET", f"/nba/trial/v7/en/league/free_agents.json?api_key={API}")
res = conn.getresponse()
data = res.read()

y = input("Now, what position are you looking for? (Input PG, SG, SF, PF, or C): ")
z = input("Years of experience: ")

if (y == "PG"):
    print("Here's a list of available Point Guards:")
if (y == "SG"):
    print("Here's a list of available Shooting Guards:")
if (y == "SF"):
    print("Here's a list of available Small Forwards:")
if (y == "SG"):
    print("Here's a list of available Power Forwards:")
if (y == "C"):
    print("Here's a list of available Centers:")
#else:
#    print("Sorry")

dict_str = data.decode("UTF-8")
mydata = ast.literal_eval(dict_str)
free_agents = mydata["free_agents"]
#pprint(free_agents)

for player in free_agents:
    if player["primary_position"] == y and player["experience"] == z:
        try:
            print(player["full_name"], player["position"], player["primary_position"], player["experience"], player["college"], player["height"], player["weight"], player["birthdate"], player["birth_place"])
        except KeyError as e:
            pass
            #source: https://realpython.com/python-keyerror/
            #source: https://stackoverflow.com/questions/15653966/ignore-keyerror-and-continue-program
            #source: https://www.toptal.com/python/top-10-mistakes-that-python-programmers-make


csv_file_path = "/Users/larrydoroger/Desktop/NBA.csv"
csv_headers = ["full_name", "position", "primary_position", "experience", "college", "height", "weight", "birthdate", "birthplace"]

with open(csv_file_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader()
    for player in free_agents:
        writer.writerow({
            "full_name": player["full_name"],
            "position": player["position"],
            "primary_position": player["primary_position"],
            "experience": player["experience"],
            "college": player["college"],
            "height": player["height"],
            "weight": player["weight"],
            "birthdate": player["birthdate"],
            "birthplace": player["birth_place"],
            })

#source: csv related: https://github.com/Fleshner/robo-advisor/blob/main/app/robo_advisor.py
#source: https://github.com/s2t2/robo-advisor-screencast/blob/v3-testing/app/robo_advisor.py