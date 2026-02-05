import random


def main():
    level = get_level()
    print(level)


def get_level():
    return input("Level: ")


def generate_integer(level):
    return random.randint(1, level)


if __name__ == "__main__":
    main()
