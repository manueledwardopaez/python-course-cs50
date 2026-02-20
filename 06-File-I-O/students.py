import csv

""" students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row['name'], "house": row['house']})

for student in sorted(students, key=lambda student: student["house"]):
    print(f"{student['name']} is in {student['house']}") """

name = input("What's your name ? ")
house = input("What's your house ? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "house"])
    writer.writerow({"name": name, "house": house})