import requests
import sys
 
try:
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")

    amountBTC = float(sys.argv[1])
    print(sys.argv[1])

    r = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=f45763b2220265bc789655b8fcc24fb9a5e4f76b0c7e5131a09146fd57e95262")
    resp = r.json()
    priceUsd = resp['data']['priceUsd']
    print(priceUsd)

    amount = amountBTC * float(priceUsd)

    print(f"${amount:,.4f}")

except ValueError:
    sys.exit("Command-line argument is not a number")
    
except requests.RequestException:
    sys.exit("An error ocurred during the request")
