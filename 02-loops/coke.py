
amount_owed = 50

while amount_owed > 0:
    inserted_coin = int(input("Insert Coin: "))
    if inserted_coin == 25 or inserted_coin == 10 or inserted_coin == 5:
        amount_owed -= inserted_coin
        print(f"Amount Owed: {amount_owed} ")
        if amount_owed < 0:
            print(f"Your change: {abs(amount_owed)} " )
    else:
        print(f"Change Owed: {amount_owed} ")
        continue

