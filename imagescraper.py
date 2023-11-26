import requests

with open("multimedia.txt",mode="r") as fl:
    lines = fl.readlines()
    for line in lines:
        row = line.split()
        if row[2]== "image/jpeg":
            try:
                print(row[3])
                response = requests.get(row[3])
                response.raise_for_status()
            except:
                print("error")