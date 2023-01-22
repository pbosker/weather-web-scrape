# This program is desinged to extract a fun fact about Chuck Norris from a website using an API call.     This fun fact is then
# written to a post on https://paulbosker.com called "chuck-norris".    This program is scheduled to run every 15 minutes using
# cronjob.

from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import EditPost
from wordpress_xmlrpc.methods import posts
import json
import requests
import base64

def edit_post(wpcontent):

#   the password in the command below is usable only using an API.   In other words, this password cannot be used by a user logging
#   onto the website in an interactive mode.
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
#   CND is the value passed from the Chuck Norris site to the post on my website.
    wpcontent = f"<h4>" + cnd + "</h4>"
    wpcontent += f"<h4></h4>"
    wpcontent += f"<p></p>"
    wpcontent += f"<p></p>"
    wpcontent += f"<p>Come back again in 5 minutes for another fun fact about Mr. Norris</p>"
    wpcontent += f"<p>Fun with API calls</p>"
    wpcontent += f"<p></p>"




    edit_post(wpcontent)
