from wordpress_xmlrpc import WordPressPost

post = WordPressPost()
post.title = 'My post'
post.content = 'This is a wonderful blog post about XML-RPC.'
print('creating')
post.id = client.call(posts.NewPost(post))

# whoops, I forgot to publish it!
print('updating post id:  ' + str(post.id))
post.post_status = 'publish'
client.call(posts.EditPost(post.id, post))
