def main():
    text = input("Write a text... ")
    result = shorten(text)
    print(result)


def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    short_text = ""

    for l in word:
        if l.lower() in vowels:
            continue
        short_text += l

    return short_text


if __name__ == "__main__":
    main()