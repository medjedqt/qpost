from .user import User

class Follow:
	'''Represents qpost's Follow object'''
	def __init__(self, followdict, bot):
		self.id: int = followdict['id'] #: The unique identifier of this Follow
		self.sender: User = User(followdict['sender'], bot) #: The creator of this Follow
		self.receiver: User = User(followdict['receiver'], bot) #: The user that was followed
		self.time_created: str = followdict['time'] #: The timestamp of when this Follow was created

class FollowRequest:
	'''Represents qpost's FollowRequest object'''
	def __init__(self, requestdict, bot):
		self.id: int = requestdict['id'] #: The unique identifier of this FollowRequest
		self.sender: User = User(requestdict['sender']) #: The creator of this FollowRequest
		self.receiver: User = User(requestdict['receiver']) #: The user that received the request
		self.time_created: str = requestdict['time'] #: The timestamp of when this FollowRequest was created
		self.bot = bot

	def accept(self):
		'''Accepts the follow request'''
		self.bot.accept_follow_request(self.id)

	def decline(self):
		'''Declines the follow request'''
		self.bot.decline_follow_request(self.id)
