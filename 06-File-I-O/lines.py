import sys

def main():

    lines_amount = 0

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if sys.argv[1].endswith(".py") == False:
        sys.exit("Not a Python file")

    try:
        with open(sys.argv[1], "r") as file:
            content = file.readlines()
            for line in content: 
                if not line.lstrip().startswith("#") and line.strip() != "":
                    lines_amount += 1
        print(lines_amount)    

    except(FileNotFoundError):
        sys.exit("File does not exist")

main()