from validator_collection import is_email

def main():
    email = input("What's your email address? ")
    validation = validate_email(email)
    print(validation)


def validate_email(email):
    if is_email(email):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()
