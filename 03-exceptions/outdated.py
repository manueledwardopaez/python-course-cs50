
months_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ").strip()
        is_text_month = False

        for m in months_list:
            if date.startswith(m):
                is_text_month = True

                if "," not in date:
                    raise ValueError

                date = date.replace(",", "")
                m, d, y = date.split(" ")
                break

        if not is_text_month:
            m, d, y = date.split("/")

        if int(d) < 1 or int(d) > 31:
            continue

        if is_text_month:
            print(f"{y}-{months_list.index(m) + 1:02}-{int(d):02}")
        else:
            if int(m) < 1 or int(m) > 12:
                continue
            print(f"{y}-{int(m):02}-{int(d):02}")

        break

    except ValueError:
        continue
