from datetime import date
import inflect
import sys


def seasons(today, DOB):
    p = inflect.engine()
    difference = today - DOB
    minutes = difference.days * 24 * 60
    return f"{p.number_to_words(minutes, andword='').capitalize()} minutes"


def main():

    try:
        year, month, day = input("DOB: ").split("-")

        year    = int(year)
        month   = int(month)
        day     = int(day)

        DOB     = date(year, month, day)
        today   = date.today()

        if DOB > today:
            sys.exit("Invalid date")

        print(seasons(today, DOB))

    except ValueError:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()