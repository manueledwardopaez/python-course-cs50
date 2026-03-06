import re

def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"\b[U-u][M-m]\b"

    match = re.findall(pattern, s)

    return(len(match))
...


if __name__ == "__main__":
    main()