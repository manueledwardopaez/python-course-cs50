import random


def main():
    level = get_level()
    score = 0
    count = 0

    while count < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        correct = x + y
        tries = 0

        while tries < 3:
            answer = input(f"{x} + {y} = ")

            try:
                if int(answer) == correct:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
            except:
                print("EEE")
                tries += 1

        if tries == 3:
            print(f"{x} + {y} = {correct}")

        count += 1

    print("Score:", score)


def get_level():
    while True:
        level = input("Level: ")
        try:
            level = int(level)
            if level == 1 or level == 2 or level == 3:
                return level
        except:
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    if level == 2:
        return random.randint(10, 99)
    if level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
