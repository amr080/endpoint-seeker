import requests

# Example URL (adjust the path)
url = "https://api.exchange.coinbase.com/"

# Send OPTIONS request to check available methods
response = requests.options(url)

print("Allowed methods:", response.headers.get("Allow"))
print("Response headers:", response.headers)
