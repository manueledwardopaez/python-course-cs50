import requests
import sys
 
try:
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")

    amountBTC = float(sys.argv[1])
    print(sys.argv[1])

    r = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=apiKey")
    resp = r.json()
    priceUsd = resp['data']['priceUsd']
    print(priceUsd)

    amount = amountBTC * float(priceUsd)

    print(f"${amount:,.4f}")

except ValueError:
    sys.exit("Command-line argument is not a number")
    
except requests.RequestException:
    sys.exit("An error ocurred during the request")
