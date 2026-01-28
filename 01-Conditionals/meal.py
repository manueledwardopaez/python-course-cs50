def main():
    time = input("What time is it? ")
    convert(time)

def convert(time):
    t = float(time.replace(":", "."))
    if 7 <= t <= 8:
        print("breakfast time")
    elif 12 <= t <= 13:
        print("lunch time")
    elif 18 <= t <= 19:
        print("dinner time")


if __name__ == "__main__":
    main()
