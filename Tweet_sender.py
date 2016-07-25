import OAuth
from urllib2 import urlopen
import re

# t = OAuth.Create_Apps()

class TweetSender(object):
	"""input the username and the index you want"""
	def __init__(self, user_name, tweet_index):
		super(TweetSender, self).__init__()
		self.user_name = user_name
		self.tweet_index = tweet_index

	def send(self):
		# Fetch image file and status text
		try:
			url = t.statuses.user_timeline(screen_name=self.user_name)[self.tweet_index]['extended_entities']['media'][0]['media_url']
			imagefile = urlopen(url)
			imagedata = imagefile.read()
			status_text = t.statuses.user_timeline(screen_name=self.user_name)[self.tweet_index]['text']

			# Send the tweet
			params = {"media[]": imagedata, "status": status_text}
			t.statuses.update_with_media(**params)

		# If there's no picture, it will raise KeyError
		except KeyError:
			status_text = t.statuses.user_timeline(screen_name=self.user_name)[self.tweet_index]['text']
			t.statuses.update(status = status_text)
		# If the text part is over 140 limit, it will raise Twitter error
		except:
			self.truncated_text_send()

	def truncated_text_send(self):
		# truncating the text
		status_text = t.statuses.user_timeline(screen_name=self.user_name)[self.tweet_index]['text']
		''' Test if it is a retweet or reply
		Note: sometimes a tweet contains two links, with the first one the link
		to a website and the latte one to the pic, and I will only erase the second one
		'''
		try:
			startpoint = re.search(r'@+\w*', status_text).end()
			endpoint = re.search(r'htt(p|ps)://[\w./]*$', status_text).start()
			status_text = status_text[startpoint+1:endpoint]
		except:
			endpoint = re.search(r'htt(p|ps)://[\w./]*$', status_text).start()
			status_text = status_text[:endpoint]
		# Tweet out the truncated text judging if there're pictures
		try:
			url = t.statuses.user_timeline(screen_name=self.user_name)[self.tweet_index]['extended_entities']['media'][0]['media_url']
			imagefile = urlopen(url)
			imagedata = imagefile.read()

			params = {"media[]": imagedata, "status": status_text}
			t.statuses.update_with_media(**params)
		except:
			t.statuses.update(status = status_text)

	def retweet(self):
		t.statuses.retweet(id=t.statuses.user_timeline(screen_name=self.user_name)[self.tweet_index]['id'])

	def log(self):
		print t.statuses.user_timeline(screen_name=self.user_name)[self.tweet_index]['text']
		print t.statuses.user_timeline(screen_name=self.user_name)[self.tweet_index]['extended_entities']['media'][0]['media_url']

if __name__ == '__main__':
	t = OAuth.Create_Apps()
	object = TweetSender('chihuo_lele', 1)
	object.log()