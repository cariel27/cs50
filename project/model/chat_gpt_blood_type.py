# Define blood types
BLOOD_TYPES = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

# Get user input for donor and recipient blood types
donor_blood_type = input("Enter donor blood type: ")
recipient_blood_type = input("Enter recipient blood type: ")

# Check if blood types are valid
if donor_blood_type not in BLOOD_TYPES or recipient_blood_type not in BLOOD_TYPES:
    print("Invalid blood type. Please enter a valid blood type.")
else:
    # Determine blood donor and recipient based on blood types
    if donor_blood_type == "O-":
        print("O- can donate to all blood types.")
    elif donor_blood_type == "O+" and recipient_blood_type in ["O+", "A+", "B+", "AB+"]:
        print("O+ can donate to O+, A+, B+, and AB+.")
    elif donor_blood_type == "A-" and recipient_blood_type in ["A-", "AB-"]:
        print("A- can donate to A- and AB-.")
    elif donor_blood_type == "A+" and recipient_blood_type in ["A+", "A-", "AB+", "AB-"]:
        print("A+ can donate to A+, A-, AB+, and AB-.")
    elif donor_blood_type == "B-" and recipient_blood_type in ["B-", "AB-"]:
        print("B- can donate to B- and AB-.")
    elif donor_blood_type == "B+" and recipient_blood_type in ["B+", "B-", "AB+", "AB-"]:
        print("B+ can donate to B+, B-, AB+, and AB-.")
    elif donor_blood_type == "AB-" and recipient_blood_type == "AB-":
        print("AB- can donate to AB-.")
    elif donor_blood_type == "AB+" and recipient_blood_type in ["AB+", "AB-"]:
        print("AB+ can donate to AB+ and AB-.")
    else:
        print("Blood type mismatch. Donor and recipient blood types are not compatible.")
