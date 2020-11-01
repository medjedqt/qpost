from .user import User

class Follow:
	'''Represents qpost's Follow object'''
	def __init__(self, followdict: dict, bot):
		self.id = followdict['id'] #: int: The unique identifier of this Follow
		self.sender = User(followdict['sender'], bot) #: :obj:`User`: The creator of this Follow
		self.receiver = User(followdict['receiver'], bot) #: :obj:`User`: The user that was followed
		self.time_created = followdict['time'] #: str: The timestamp of when this Follow was created

class FollowRequest:
	'''Represents qpost's FollowRequest object'''
	def __init__(self, requestdict: dict, bot):
		self.id = requestdict['id'] #: int: The unique identifier of this FollowRequest
		self.sender = User(requestdict['sender']) #: :obj:`User`: The creator of this FollowRequest
		self.receiver = User(requestdict['receiver']) #: :obj:`User`: The user that received the request
		self.time_created = requestdict['time'] #: str: The timestamp of when this FollowRequest was created
		self.bot = bot

	def accept(self):
		'''Accepts the follow request'''
		self.bot.accept_follow_request(self.id)

	def decline(self):
		'''Declines the follow request'''
		self.bot.decline_follow_request(self.id)
