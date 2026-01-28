text = input("Write a text... ")
vowels = ["a", "e", "i", "o", "u"]
short_text = ""

for l in text:
    if l.lower() in vowels:
        continue

    short_text += l

print(short_text)
