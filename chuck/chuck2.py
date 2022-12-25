from wordpress_xmlrpc import Client, WordPressPost
#from wordpress_xmlrpc.methods.posts import NewPost
from wordpress_xmlrpc.methods.posts import EditPost
from wordpress_xmlrpc.methods import posts
import json
import requests
import base64

def edit_post(wpcontent):

    wp = Client('https://paulbosker.com/xmlrpc.php', 'paul', 'Bd0E pWaM sImJ OXoj DrlI QwGn')

    post = WordPressPost()
    post.id = '59593'
    post.title = f"Chuck Norris"
    post.content = wpcontent
    post.terms_names = {'category': ['Chuck Norris']}
    post.post_status = "publish"
    post.id=wp.call(EditPost(post.id, post))

if __name__ == '__main__':
    url_in = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"
    header1 = {
            "accept": "application/json",
            "X-RapidAPI-Key": "59cf99f2d8mshd1a719884ee4f3cp154303jsna5cde8628710",
            "X-RapidAPI-Host": "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
    }

    response1 = requests.request("GET", url_in, headers=header1)
    cn = json.loads(response1.text)
    cnd = cn["value"]
    wpcontent = f"<p>" + cnd + "</p>"

 #   print(str(wpcontent))
    edit_post(wpcontent)
