import sys
import requests

try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line agrument")
    

    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=1f50c884fbca49755784073747fbdf14635bda134fe15f4dd576e15d05218a09")
    o = response.json()
    price = float(o["data"]["priceUsd"])
    cost = price * float(sys.argv[1])
    print(f"${cost:,.4f}")
except requests.RequestException as e:
    sys.exit(f"Request Error: {e}")
except ValueError as e:
    sys.exit(f"Request Error: {e}")
    










