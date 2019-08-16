import requests

url = "https://interns.bcgdvsydney.com/api/v1/key"

headers = {
    'cache-control': "no-cache",
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
print("\n")
print(response.status_code)