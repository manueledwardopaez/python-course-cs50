import csv
import sys
from tabulate import tabulate

def main():
    # Sys Arguments validation 
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if sys.argv[1].endswith(".csv") == False:
        sys.exit("Not a CSV file")

    data_list = []

    try:
        # Open cvs and place all rows into data_list
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                data_list.append(row)
            
        print(tabulate(data_list, headers="keys", tablefmt="grid"))

    except(FileNotFoundError):
        sys.exit("File does not exist")

main()