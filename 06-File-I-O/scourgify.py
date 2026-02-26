import csv
import sys


def main():
    # Validación de argumentos
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        students = []

        # Leer archivo de entrada
        with open(sys.argv[1], "r") as infile:
            reader = csv.DictReader(infile)

            for row in reader:
                last, first = row["name"].split(",")

                students.append({
                    "first": first.strip(),
                    "last": last.strip(),
                    "house": row["house"]
                })

        # Escribir archivo de salida
        with open(sys.argv[2], "w", newline="") as outfile:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(students)

    except FileNotFoundError:
        sys.exit("File does not exist")


main()