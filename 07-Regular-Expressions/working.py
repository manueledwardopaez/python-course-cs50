import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    first_hour_to_show = ""
    second_hour_to_show = ""
    # Get user input

    # Split using the to as a separator
    first_hour , second_hour = s.split(" to ")

    # Check each time pattern. If digit 1 is > 12, ValueError.    
    # if digit 2 is > 5, ValueError
    # if digit 3 is > 9, ValueError

    pattern = r"^(0?[1-9]|1[0-2]):?([0-5][0-9])? (AM|PM)$" 
    first_hour_match  = re.fullmatch(pattern, first_hour)
    second_hour_match = re.fullmatch(pattern, second_hour)

    if first_hour_match == None or second_hour_match == None:
        raise ValueError()
    

    # Si times es 12 am, retorno 00:00.
    # Si es de 1 am 11 am, retorna igual sin am.
    # Si es 12 pm retorna 12
    # Si es de 1 pm a 11pm retorna eso mas 12. 
    if first_hour_match.group().endswith("AM"):
        first_hour = first_hour.replace(" AM", "")
        parts = first_hour.split(":", 1)
        first_hour_1 = parts[0]
        first_hour_2 = parts[1] if len(parts) > 1 else "00"
        if first_hour_1 == "12":
            first_hour_1 = 0
        first_hour_to_show = (f"{int(first_hour_1):02}:{first_hour_2:02}")

    if first_hour_match.group().endswith("PM"):
        first_hour = first_hour.replace(" PM", "")
        parts = first_hour.split(":", 1)
        first_hour_1 = parts[0]
        first_hour_2 = parts[1] if len(parts) > 1 else "00"
        if first_hour_1 != "12":
            first_hour_1 = int(first_hour_1) + 12
            first_hour_to_show = (f"{int(first_hour_1):02}:{first_hour_2:02}")
        else:
            first_hour_to_show = (f"{int(first_hour_1):02}:{first_hour_2:02}")

    if second_hour_match.group().endswith("AM"):
        second_hour = second_hour.replace(" AM", "")
        parts = second_hour.split(":", 1)
        second_hour_1 = parts[0]
        second_hour_2 = parts[1] if len(parts) > 1 else "00"
        if second_hour_1 == "12":
            second_hour_1 = 0
        second_hour_to_show = (f"{int(second_hour_1):02}:{second_hour_2:02}")

    if second_hour_match.group().endswith("PM"):
        second_hour = second_hour.replace(" PM", "")
        parts = second_hour.split(":", 1)
        second_hour_1 = parts[0]
        second_hour_2 = parts[1] if len(parts) > 1 else "00"
        if second_hour_1 != "12":
            second_hour_1 = int(second_hour_1) + 12
            second_hour_to_show = (f"{int(second_hour_1):02}:{second_hour_2:02}")
        else:
            second_hour_to_show = (f"{int(second_hour_1):02}:{second_hour_2:02}")


    # Print both times converted

    return f"{first_hour_to_show} to {second_hour_to_show}"


if __name__ == "__main__":
    main()
