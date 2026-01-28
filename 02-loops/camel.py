
str = input("Enter your camel case string: ")

snake_case = ""

for letter in str:
    if letter.isupper():
        snake_case += "_" + letter.lower()
    else: 
        snake_case += letter


print(snake_case)
