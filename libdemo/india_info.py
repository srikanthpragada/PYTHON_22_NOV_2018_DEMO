import requests
import sys

code = input("Enter country code :")
resp = requests.get(f"https://restcountries.eu/rest/v2/alpha/{code}")
if resp.status_code != 200:
    print("Sorry! Could not get details..")
    sys.exit(0)

details = resp.json()
for k,v in details.items():
    print(f"{k:20s}  {v}")


