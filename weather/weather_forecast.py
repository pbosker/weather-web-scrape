import requests

url = "https://weather-by-api-ninjas.p.rapidapi.com/v1/weather"

querystring = {"city":"Orlando"}

headers = {
	"X-RapidAPI-Key": "59cf99f2d8mshd1a719884ee4f3cp154303jsna5cde8628710",
	"X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
