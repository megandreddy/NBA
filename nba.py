import ast
import os
import http.client
from dotenv.main import load_dotenv
import csv
load_dotenv()
from pprint import pprint

API = os.getenv("api_key")
print("Welcome to the Free Agent Search Tool!")
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
dict_str = data.decode("UTF-8")
mydata = ast.literal_eval(dict_str)
free_agents = mydata["free_agents"]

clean_players = []
for player in free_agents:
    clean_player = {}

    try:
        clean_player["name"] = player["full_name"]
    except KeyError:
        clean_player["name"] = "N/A"
    try:
        clean_player["general_position"] = player["position"]
    except KeyError:
        clean_player["general_position"] = "N/A"
    try:
        clean_player["position"] = player["primary_position"]
    except KeyError:
        clean_player["position"] = "N/A"
    try:
        clean_player["experience"] = player["experience"]
    except KeyError:
        clean_player["experience"] = 0
    try:
        clean_player["college"] = player["college"]
    except KeyError:
        clean_player["college"] = "N/A"
    try:
        clean_player["height"] = float(player["height"])
    except KeyError:
        clean_player["height"] = "N/A"
    try:
        clean_player["weight"] = float(player["weight"])
    except KeyError:
        clean_player["height"] = "N/A"
    try:
        clean_player["birthdate"] = player["birthdate"]
    except KeyError:
        clean_player["birthdate"] = "N/A"
    try:
        clean_player["birthplace"] = player["birth_place"]
    except KeyError:
        clean_player["birthplace"] = "N/A"
    clean_players.append(clean_player)
#source: Professor Rossetti in class 10 explained how to convert our orginal data to a clean list

for player in clean_players:
    try:
        print(f'Player Name: {player["name"]}, Position: ({player["general_position"]}), Primary Position: ({player["position"]}), Years of Experience: ({player["experience"]}), College: {player["college"]}, Height (inches): ({player["height"]}), Weight (lbs): ({player["weight"]}), Birthdate: ({player["birthdate"]}), Place of Birth: {player["birthplace"]}')
    except KeyError as e:
        pass

y = input("Now, what position are you looking for? (Input PG, SG, SF, PF, or C): ")
z = input("Years of experience: ")

if (y == "PG"):
    print(f"Here's a list of available Point Guards: with {z} years of experience")
if (y == "SG"):
    print(f"Here's a list of available Shooting Guards: with {z} years of experience")
if (y == "SF"):
    print(f"Here's a list of available Small Forwards: with {z} years of experience")
if (y == "SG"):
    print(f"Here's a list of available Power Forwards: with {z} years of experience")
if (y == "C"):
    print(f"Here's a list of available Centers: with {z} years of experience")
else:
    print(f"Sorry currently no {y} players with {z} years of experience are available.")

query_list = []
for player in clean_players:
    if player["position"] == y and player["experience"] == z:
        print(f'Player Name: {player["name"]}, Position: ({player["general_position"]}), Primary Position: ({player["position"]}), Years of Experience: ({player["experience"]}), College: {player["college"]}, Height (inches): ({player["height"]}), Weight (lbs): ({player["weight"]}), Birthdate: ({player["birthdate"]}), Place of Birth: {player["birthplace"]}')
        query_list.append(player)
    if KeyError:    
        pass        
#source: https://realpython.com/python-keyerror/
#source: https://stackoverflow.com/questions/15653966/ignore-keyerror-and-continue-program
#source: https://www.toptal.com/python/top-10-mistakes-that-python-programmers-make

to_csv = input("Would you like a copy of this information in CSV? (Type Yes or No) ")
if to_csv.upper() == "YES":
    csv_file_path = "/Users/larrydoroger/Desktop/NBA.csv"
    csv_headers = ["full_name", "position", "primary_position", "experience", "college", "height", "weight", "birthdate", "birthplace"]
    with open(csv_file_path, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
        writer.writeheader()
        for player in query_list:
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
else:
    print("Thank You!")
    exit()