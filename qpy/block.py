from .user import User

class Block:
	'''Represents qpost's Block object'''
	def __init__(self, blockdict, bot):
		self.id: int = blockdict['id'] #: The unique identifier of this Block
		self.user: User = User(blockdict['user']) #: The creator of this Block
		self.target: User = User(blockdict['target']) #: The user that was blocked
		self.time_created: str = blockdict['time'] #: The timestamp of when this Block was created
		self.bot = bot
	
	def delete(self):
		'''Removes block'''
		self.bot.unblock(self.user.id)
