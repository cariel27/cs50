
students = []

with open(file="students.csv", mode="r") as file:
    for line in file:
        name, house = line.strip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in sorted(students, key=lambda s: s["name"]):
    print(f"{student['name']} is in {student['house']}")

