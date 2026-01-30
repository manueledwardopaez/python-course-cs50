while True:
    try:
        fraction = input("Enter fraction: ")
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        if x > y:
            continue
        elif x < 0 or y < 0:
            continue
        result = round((x / y) * 100)
    except (ValueError, ZeroDivisionError):
        continue
    else:
        if result <= 1:
            print("E")
        elif result >= 99:
            print("F")
        else:
            print(f"{result}%")
        break