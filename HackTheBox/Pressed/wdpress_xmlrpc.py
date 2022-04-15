#!/usr/bin/python

from wordpress_xlmrpc import Client
from wordpress_xlmrpc.methods import posts

client = Client("http://pressed.htb/xmlrpc.php",'admin','uhc-jan-finals-2022')
post =  client.call(posts.GetPosts())
post
