from .user import User

class Follow:
	def __init__(self, followdict: dict, bot):
		'''Represents qpost's Follow object'''
		self.id = followdict['id']
		self.sender = User(followdict['sender'], bot)
		self.receiver = User(followdict['receiver'], bot)
		self.time_created = followdict['time']

class FollowRequest:
	def __init__(self, requestdict: dict, bot):
		'''Represents qpost's FollowRequest object'''
		self.id = requestdict['id']
		self.sender = User(requestdict['sender'])
		self.receiver = User(requestdict['receiver'])
		self.time_created = requestdict['time']
		self.bot = bot

	def accept(self):
		self.bot.accept_follow_request(self.id)

	def decline(self):
		self.bot.decline_follow_request(self.id)
