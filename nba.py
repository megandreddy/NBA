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

#print("-------------------------")

x = input("Do you want to find the best player for your team? (Type Yes or No): ")
    if x.upper() == "NO": #source - .upper https://github.com/s2t2/shopping-cart-with-email-receipts/blob/master/checkout.py
        exit
    else:
        try:
            conn = http.client.HTTPSConnection("api.sportradar.us")
            conn.request("GET", f"/nba/trial/v7/en/league/free_agents.json?api_key={API}")
            res = conn.getresponse()
            data = res.read()
            #pprint(data)
            #print(type(data))
            #print(data.keys())
            # source: https://stackoverflow.com/questions/49184578/how-to-convert-bytes-type-to-dictionary
            dict_str = data.decode("UTF-8")
            mydata = ast.literal_eval(dict_str)
            #print(repr(mydata))
            print(type(mydata))
            print(mydata.keys())
            pprint(mydata)
            print("Now, what position are you looking for? (Input PG, SG, SF, PF, or C):")
        except IndexError as e:
            print("Goodbye!")
            #source: https://github.com/larrydor/shopping_cart    

#while True:
    x = input("Do you want to find the best player for your team? (Type Yes or No): ")
    if x.upper() == "NO": #source - .upper https://github.com/s2t2/shopping-cart-with-email-receipts/blob/master/checkout.py
        break
    else:
        try:
            conn = http.client.HTTPSConnection("api.sportradar.us")
            conn.request("GET", f"/nba/trial/v7/en/league/free_agents.json?api_key={API}")
            res = conn.getresponse()
            data = res.read()
            #pprint(data)
            #print(type(data))
            #print(data.keys())
            # source: https://stackoverflow.com/questions/49184578/how-to-convert-bytes-type-to-dictionary
            dict_str = data.decode("UTF-8")
            mydata = ast.literal_eval(dict_str)
            #print(repr(mydata))
            print(type(mydata))
            print(mydata.keys())
            pprint(mydata)
            print("Now, what position are you looking for? (Input PG, SG, SF, PF, or C):")
        except IndexError as e:
            print("Goodbye!")
            break
            #source: https://github.com/larrydor/shopping_cart    