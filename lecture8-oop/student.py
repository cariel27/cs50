# status: https://youtu.be/e4fwY9ZsxPw?t=4059

class Student:
    def __init__(self, name: str, house: str):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Russell terrier":
                return "🐶"
            case _:
                return "🪄"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house: str):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name=name, house=house)


def main():
    student = Student.get()
    # This will fail
    # student.house = "Leo house"
    print(student)


if __name__ == "__main__":
    main()
