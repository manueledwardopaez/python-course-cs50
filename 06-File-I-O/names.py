###    
    #
""" name = input("What's your name ? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n") """

""" with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines: 
    print("Hello, ", line.rstrip()) """
#wwewewe
names = []
    # sdsdsdd
with open("names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"Hello, {name}")