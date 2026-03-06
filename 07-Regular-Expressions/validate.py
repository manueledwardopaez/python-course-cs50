import re

email = input("What's your email ? : ")

if re.search(r"^\w+@\w+.+\edu$", email):
    print("Valid")
else:
    print("Invalid")