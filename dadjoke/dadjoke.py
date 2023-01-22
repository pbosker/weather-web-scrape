from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import EditPost
from wordpress_xmlrpc.methods import posts
import json
import requests
import base64

def edit_post(wpcontent):
    wp = Client('https://paulbosker.com/xmlrpc.php', 'paul', 'Bd0E pWaM sImJ OXoj DrlI QwGn')
    post = WordPressPost()
    post.id = '62871'
    post.title = f"Dad Jokes"
    post.content = wpcontent
    post.terms_names = {'category': ['Humor']}
    post.post_status = "publish"
    post.id=wp.call(EditPost(post.id, post))

if __name__ == '__main__':
    url = "https://jokeapi-v2.p.rapidapi.com/joke/Any"

    querystring = {"format":"json","contains":"C%23","idRange":"0-150","blacklistFlags":"nsfw,racist"}

    headers = {
	"X-RapidAPI-Key": "59cf99f2d8mshd1a719884ee4f3cp154303jsna5cde8628710",
	"X-RapidAPI-Host": "jokeapi-v2.p.rapidapi.com"
    }
    response1 = requests.request("GET", url, headers=headers)
    cn = json.loads(response1.text)
    cns = cn["setup"]
    cnd = cn["delivery"]
    cnf = cn["flags"]
    cnfrg = cnf["religious"]
    cnfrc = cnf["racist"]
    cnfex = cnf["explicit"]

#   if the joke is not considered religious, racist, or explicit, then procede, otherwise skip it
    if (cnfrg == False) and (cnfrc == False) and (cnfex == False):
        wpcontent = f"<h4>" + cns + "</h4>"
        wpcontent += f"<h4>" + cnd + "</h4>"
        wpcontent += f"<p></p>"
        wpcontent += f"<p></p>"
        wpcontent += f"<p>Come back again in 5 minutes for another fun Dad Joke</p>"
        wpcontent += f"<p>Fun with API calls</p>"
        wpcontent += f"<p></p>"
        edit_post(wpcontent)
    else:
        print("Inappropriate Joke")

