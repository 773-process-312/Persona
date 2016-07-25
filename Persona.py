from twitter import *
from urllib2 import urlopen

t = Twitter(auth=OAuth(
	token = '1123675933-GwbZE82ViIKAE2VgUURVSPDajncRmUF9YoPYrtT', 
	token_secret ='wMKFaoIOeRhqCNBwvsGVqySZXuuQcaSxwOZOUVEHkLas3', 
	consumer_key = 'Fd517TO2djxoMNeXRE1jthbYq', 
	consumer_secret = 'JKfstopO6kMY8dHXwOlVg6RxqZupLnBJeVnT0NskmttWHeRVR2'))

# print t.statuses.home_timeline()

# Get your "home" timeline
# for i in t.statuses.home_timeline():
# 	print i['text']

# Fetch image file and status text
url = t.statuses.user_timeline(screen_name="chihuo_lele")[1]['extended_entities']['media'][0]['media_url']
imagefile = urlopen(url)
imagedata = imagefile.read()

status_text = t.statuses.user_timeline(screen_name="chihuo_lele")[1]['text']

# Send the tweet
params = {"media[]": imagedata, "status": status_text}
t.statuses.update_with_media(**params)