import csv
students = []

with open(file="students_for_csv.csv", mode="r") as file:
    # Previous approach:
    # reader = csv.reader(file)

    # After adding col name to csv file I can use DictReader
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda s: s["name"]):
    print(f"{student['name']} is in {student['home']}")

