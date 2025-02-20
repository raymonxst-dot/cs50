import requests
import sys
try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    elif sys.argv[1].isalpha:
        sys.exit("Missing command-line argument")
    else:
        x = requests.get("https://api.coincap.io/v2/assets/bitcoin")
        info=x.json()
        price=info["data"]["priceUsd"]
        total=float(price)*float(sys.argv[1])
        print(f"${total:,.4f}")
except requests.RequestException:
    pass