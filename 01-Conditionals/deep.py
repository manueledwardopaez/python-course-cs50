answer = input("Whats the answer ? ").lower().replace(" ", "").replace("-", "").replace("_", "")


if answer == "42" or answer == "fortytwo":
    print("Yes")
else:
    print("No")