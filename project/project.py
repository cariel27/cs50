from model.blood_type import BloodType
import sys

blood_options = {"1": "A +", "2": "A -", "3": "B +", "4": "B -", "5": "AB +", "6": "AB -", "7": "O +", "8": "O -"}


def select_blood():
    # Get user input for donor and recipient blood types
    print("#" * 65)
    for k, v in blood_options.items():
        print(f"{k}) {v}")
    print("or Press 'Q' to exit", end="\n")
    print("#" * 65)
    while True:
        option = input("Select blood type: ")
        if option in blood_options.keys():
            return blood_options[option]
        elif option.upper() == "Q":
            sys.exit("Bye.")


def main():
    antigen, protein = select_blood().split(" ")
    patient_blood_type = BloodType(antigen=antigen, protein=protein)

    a = BloodType.get_compatible_donors(recipient_blood_type=patient_blood_type)
    print(a)
    # b = BloodType.get_compatible_receipts(donor_blood_type=patient_blood_type)
    # print(b)


if __name__ == "__main__":
    main()
