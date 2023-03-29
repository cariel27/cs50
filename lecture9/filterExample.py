GRIFFINDOR = "Griffindor"
SLYTHERIN = "Slytherin"

students = [
    {"name": "Hermione", "house": GRIFFINDOR},
    {"name": "Harry", "house": GRIFFINDOR},
    {"name": "Ron", "house": GRIFFINDOR},
    {"name": "Draco", "house": SLYTHERIN}
]

# List comprehension
# gryffindors = [student["name"] for student in students if student["house"] == GRIFFINDOR]

# Filter


def is_gryffindor(s):
    return s["house"] == GRIFFINDOR


gryffindors = filter(is_gryffindor, students)

for gryffindor in sorted(gryffindors, key=lambda g: g["name"]):
    print(gryffindor["name"])
