from twitter import *

def Create_Apps():
	app = Twitter(auth=OAuth(
		token = '1123675933-bck1BCvRTkQHII2ahOghKxp9VBLnIZHGH7FkulV', 
		token_secret ='VTEjd4xlueZag9h0voaZNKBdCBmQX1EwPjEF6ZnWBzYLM', 
		consumer_key = 'U3ydJHVnlWOY3Cfp71pfZHKgR', 
		consumer_secret = 'VHuhvk1N7pYtjZXpj9vttqGIoVHHIms94WtItM6rppsKU4JYkE'))
	return app

if __name__ == '__main__':
	print Create_Apps()