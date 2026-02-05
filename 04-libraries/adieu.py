import inflect

p = inflect.engine()

names = []

while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        print(f"\nAdieu, adieu, to {p.join((names), conj='and')}")
        break

