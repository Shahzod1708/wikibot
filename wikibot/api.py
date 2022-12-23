import requests
import json

# Where USD is the base currency you want to use
url = 'https://v6.exchangerate-api.com/v6/e2f0123a768eff54090e5aec/latest/UZS'

# Making our request
response = requests.get(url)
data = response.json()

# Your JSON object
#print(data)

#print(data.keys())

b = (data['conversion_rates'])
print(b)

for k in b:
    print(f"{k}:{b[k]}")
