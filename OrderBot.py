import requests

url = "https://open-ai21.p.rapidapi.com/getbotdetails"

payload = { "bot_id": "ZALuT2TU6Y4JYgQdq3ATuERyJLXK14dwHbE171099546808BrS3AAyl1QnloDpg8i2VLl8rSjwgS6k55um"}
headers = {
	"x-rapidapi-key": "5b899fe357msh7053521892e8476p18b54cjsn242e80188772",
	"x-rapidapi-host": "open-ai21.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())