from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts

client = Client('https://paulbosker.com/xmlrpc.php', 'paul', 'Bd0E pWaM sImJ OXoj DrlI QwGn')

# set to the path to your file
filename = '/home/paul/python/page0.jpg'

# prepare metadata
data = {
        'name': 'picture.jpg',
        'type': 'image/jpeg',  # mimetype
}

#data['type'] = mimetypes.read_mime_types(filename) or mimetypes.guess_type(filename)[0]

# read the binary file and let the XMLRPC library encode it into base64
with open(filename, 'rb') as img:
        data['bits'] = xmlrpc_client.Binary(img.read())

response = client.call(media.UploadFile(data))
# response == {
#       'id': 6,
#       'file': 'picture.jpg'
#       'url': 'http://www.example.com/wp-content/uploads/2012/04/16/picture.jpg',
#       'type': 'image/jpeg',
# }
attachment_id = response['id']
