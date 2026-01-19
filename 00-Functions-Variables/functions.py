def main():
    name = input("What is your name? ")
    hello(name)

def hello(name = "Everyone"):
    print("hello,", name)


main()