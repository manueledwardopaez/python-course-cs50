def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if len(s) < 2 or len(s) > 6:
        return False

    if not s[0].isalpha() or not s[1].isalpha():
        return False

    for c in s:
        if not c.isalnum():
            return False

    numbers_started = False

    for c in s:
        if c.isdigit():
            if not numbers_started:
                if c == "0":
                    return False
                numbers_started = True
        else:
            if numbers_started:
                return False

    return True


if __name__ == "__main__":
    main()
