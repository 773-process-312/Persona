import OAuth
import random
from Tweet_sender import TweetSender

class RandamTweeter(object):
	"""docstring for RandamTweeter"""
	def __init__(self, level, sample_size, method):
		super(RandamTweeter, self).__init__()
		self.level = level
		self.sample_size = sample_size # should be less than 200
		self.method = method

	def parser(self):
		global screen_name, file
		if self.level == 0:
			file = t.statuses.home_timeline(count=self.sample_size)
		elif self.level == 1:
			screen_name = t.statuses.home_timeline(count=self.sample_size)['user']['screen_name']
			# user_id =  t.statuses.home_timeline(count=self.sample_size)[index]['id']
			file = t.statuses.user_timeline(screen_name=screen_name, count=self.sample_size)
		elif self.level == 2:
			self.level = random.choice([0,1])
			self.parser()
		else:
			# 'Wrong options, please use 0, 1 or 2'
			raise SyntaxError('Wrong options, please use 0, 1 or 2')
		return file

	def Randomizer(self):
		file = self.parser()
		index = random.choice(list(range(0,self.sample_size)))
		if self.method == 'send':
			sender = TweetSender(screen_name,index)
			sender.send()
		elif self.method == 'retweet':
			t.statuses.retweet(id=file[index]['id'])
		elif self.method == 'combine':
			self.method = random.choice(['send','retweet'])
			self.Randomizer()
		else:
			raise SyntaxError('Please use send, retweet or combine')

class A_Basket_Of_Users(object):
	"""docstring for RandamTweeter"""
	def __init__(self, basket, sample_size, method):
		super(A_Basket_Of_Users, self).__init__()
		self.basket = basket
		self.sample_size = sample_size # should be less than 200
		self.method = method

		holder = self.file_handler()
		self.user_index = random.choice(list(range(0,holder)))

	def file_handler(self):
		if isinstance(self.basket, list):
			holder = len(self.basket)
			return holder
		else:
			raise TypeError('Please input a list')

	def parser(self):
		global screen_name
		try:
			screen_name = self.basket[self.user_index]
			data = t.statuses.user_timeline(screen_name=screen_name,
				count=self.sample_size)
			return data
		except:
			raise SyntaxError('Check the spelling of username')

	def Randomizer(self):
		file = self.parser()
		index = random.choice(list(range(0,self.sample_size)))
		if self.method == 'send':
			sender = TweetSender(screen_name,index)
			sender.send()
		elif self.method == 'retweet':
			t.statuses.retweet(id=file[index]['id'])
		elif self.method == 'combine':
			self.method = random.choice(['send','retweet'])
			self.Randomizer()
		else:
			raise SyntaxError('Please use send, retweet or combine')

if __name__ =='__main__':
	t = OAuth.Create_Apps()
	# Persona = RandamTweeter(3, 5, 'combine')
	# Persona.Randomizer()
	Persona = A_Basket_Of_Users(['verge','cnn'], 5, 'retweet')
	Persona.Randomizer()

