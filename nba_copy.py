#import json
import ast
from pprint import pprint
#import re
#import statistics
#import requests
import os
import http.client
from dotenv import dotenv_values
from dotenv.main import load_dotenv
load_dotenv()

API = os.getenv("api_key")

print("Do you have what it takes to be a GM?")
print("-------------------------")
x = input("Do you want to find the best player for your team? (Type Yes or No): ")
if x.upper() == "NO": #source - .upper https://github.com/s2t2/shopping-cart-with-email-receipts/blob/master/checkout.py
    exit()
else:
    conn = http.client.HTTPSConnection("api.sportradar.us")
    conn.request("GET", f"/nba/trial/v7/en/league/free_agents.json?api_key={API}")
    res = conn.getresponse()
    data = res.read()
    dict_str = data.decode("UTF-8")
    mydata = ast.literal_eval(dict_str)
    free_agents = mydata["free_agents"]
    #pprint(free_agents)
    for player in free_agents:
        print(player["full_name"], player["position"], player["height"], player["weight"], player["birthdate"])
        #print(player["position"])
        #for player in mydata:
        #print(player["full_name"], player["primary_position"])




#while True:
#    x = input("Do you want to find the best player for your team? (Type Yes or No): ")
#    if x.upper() == "NO": #source - .upper https://github.com/s2t2/shopping-cart-with-email-receipts/blob/master/checkout.py
#        break
#    else:
#        try:
#            conn = http.client.HTTPSConnection("api.sportradar.us")
#            conn.request("GET", f"/nba/trial/v7/en/league/free_agents.json?api_key={API}")
#            res = conn.getresponse()
#            data = res.read()
#            #pprint(data)
#            #print(type(data))
#            #print(data.keys())
#            # source: https://stackoverflow.com/questions/49184578/how-to-convert-bytes-type-to-dictionary
#            dict_str = data.decode("UTF-8")
#            mydata = ast.literal_eval(dict_str)
#            #print(repr(mydata))
#            #for player in mydata:
#            #print(player["full_name"], player["primary_position"])
#            #print(type(mydata))
#            #print(mydata.keys())
#            #print(my_data["free_agents"].keys())
#            pprint(mydata)
#            print("Now, what position are you looking for? (Input PG, SG, SF, PF, or C):")
#        except IndexError as e:
#            print("Goodbye!")
#        #source: https://github.com/larrydor/shopping_cart









import json
import re
import statistics
import requests
import ast
import os
import http.client
from dotenv import dotenv_values
from dotenv.main import load_dotenv
from pprint import pprint
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

#print(data)

y = input("Now, what position are you looking for? (Input PG, SG, SF, PF, or C): ")
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

z = input("Years of experience: ")

dict_str = data.decode("UTF-8")
mydata = ast.literal_eval(dict_str)
free_agents = mydata["free_agents"]
#pprint(free_agents)

for player in free_agents:
    if player["primary_position"] == y:
        try:
            print(player["full_name"], player["position"], player["primary_position"], player["experience"], player["college"], player["height"], player["weight"], player["birthdate"], player["birth_place"])
        except KeyError:
            pass
            #source: https://realpython.com/python-keyerror/
            #source: https://stackoverflow.com/questions/15653966/ignore-keyerror-and-continue-program
