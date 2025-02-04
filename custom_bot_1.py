import requests

url = "https://open-ai21.p.rapidapi.com/conversationgpt35"

payload = {
	"messages": [
		{
			"role": "user",
			"content": "hello"
		}
	],
	"web_access": False,
	"system_prompt": "",
	"temperature": 0.9,
	"top_k": 5,
	"top_p": 0.9,
	"max_tokens": 256
}
headers = {
	"x-rapidapi-key": "5b899fe357msh7053521892e8476p18b54cjsn242e80188772",
	"x-rapidapi-host": "open-ai21.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())