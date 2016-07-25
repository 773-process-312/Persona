from twitter import *

def Create_Apps():
	app = Twitter(auth=OAuth(
		token = '-------------------------', 
		token_secret ='-----------------------', 
		consumer_key = '---------------------------', 
		consumer_secret = '-----------------------------'))
	return app

if __name__ == '__main__':
	print Create_Apps()
