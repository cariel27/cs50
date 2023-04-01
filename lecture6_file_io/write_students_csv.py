import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open(file="new_students.csv", mode="a") as file:
    # writer = csv.writer(file)
    writer = csv.DictWriter(f=file, fieldnames=["name", "home"])
    writer.writerow({"home": home, "name": name})


