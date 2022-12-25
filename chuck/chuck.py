import json
import requests
import base64

url_in = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"
url = "https://paulbosker.com/2022/12/17"

user = 'paul'
password = 'Bd0E pWaM sImJ OXoj DrlI QwGn'
creds = user + ":" + password
print(creds)

token = base64.b64encode(creds.encode())
wordpress_header = {'Authorization': 'Basic ' + token.decode('utf-8')}
post_id = '59544'

header1 = {
	"accept": "application/json",
	"X-RapidAPI-Key": "59cf99f2d8mshd1a719884ee4f3cp154303jsna5cde8628710",
	"X-RapidAPI-Host": "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
}

response1 = requests.request("GET", url_in, headers=header1)

cn = json.loads(response1.text)
cnd = cn["value"]

post = {
        "title" : "This is WordPress Python Integration Testing",
        "content" : "Hello, this content Python Integration",
        "status" : "publish",
        "slug" : "test slug",
        "date" : "2022-11-11T11:00:00"
}

response2 = requests.post(url, data=wordpress_header, json=post)

print('URL: ' + url)
print('wordpress header: ' + str(wordpress_header))
print('post: ' + str(post))
print("Response2:  " + str(response2))
print(cnd)

