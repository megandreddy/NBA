import csv
from nba import query_list 
#source: https://stackoverflow.com/questions/17255737/importing-variables-from-another-file

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