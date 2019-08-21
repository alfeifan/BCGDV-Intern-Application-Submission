import requests

url = "https://interns.bcgdvsydney.com/api/v1/submit"

querystring = {"apiKey":"...Enter API Key here..."}

payload = "{\n  \"name\": \"Alan Li\",\n  \"email\": \"alanfeifan.li@gmail.com\"\t\n}"
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)
print("\n", response.status_code)
