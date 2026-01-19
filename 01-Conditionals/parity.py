def main():
    x = int(input("What is X ? "))
    if is_even(x):
        print("Is Even")
    else: 
        print("Is Odd")

def is_even(num):
    return True if num % 2 == 0 else False

main()