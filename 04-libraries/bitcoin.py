import requests
import sys
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("COINCAP_API_KEY")

try:
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")

    amountBTC = float(sys.argv[1])
    print(sys.argv[1])

    r = requests.get(f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}")
    resp = r.json()
    priceUsd = resp['data']['priceUsd']
    print(priceUsd)

    amount = amountBTC * float(priceUsd)

    print(f"${amount:,.4f}")

except ValueError:
    sys.exit("Command-line argument is not a number")
    
except requests.RequestException:
    sys.exit("An error ocurred during the request")
