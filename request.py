import requests

url = "https://open-ai21.p.rapidapi.com/getimgurl"

payload = {}
headers = {
	"x-rapidapi-key": "5b899fe357msh7053521892e8476p18b54cjsn242e80188772",
	"x-rapidapi-host": "open-ai21.p.rapidapi.com",
	"Content-Type": "application/x-www-form-urlencoded"
}

response = requests.post(url, data=payload, headers=headers)

print(response.json())