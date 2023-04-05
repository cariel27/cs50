class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")


class Student(Wizard):
    def __init__(self, name: str, house: str):
        super().__init__(name=name)
        self. house = house


class Professor(Wizard):
    def __init__(self, name: str, subject: str):
        super().__init__(name=name)
        self.subject = subject


student = Student(name="Harry", house="Gryffindor")
professor = Professor(name="Severus", subject="Defense against the dark arts")

