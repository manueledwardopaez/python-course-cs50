import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.fullmatch(r"\d+\.\d+\.\d+\.\d+", ip)
    if not match:
        return False

    parts = ip.split(".")

    for part in parts:
        if part == "":
            return False

        if not 0 <= int(part) <= 255:
            return False

        if part != "0" and part.startswith("0"):
            return False

    return True


if __name__ == "__main__":
    main()