from random import choice

user_input = "Y"


while user_input == "Y":
    coin = choice(["Cara", "Cruz", "Canto"])
    print(coin)
    user_input = input("Desea seguir Y/N").upper()

