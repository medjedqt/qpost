from .core import Qpost
from .user import User

class Block:
	'''Represents qpost's Block object'''
	def __init__(self, blockdict: dict, bot: Qpost):
		self.id = blockdict['id'] #: int: The unique identifier of this Block
		self.user = User(blockdict['user']) #: :obj:`User`: The creator of this Block
		self.target = User(blockdict['target']) #: :obj:`User`: The user that was blocked
		self.time_created = blockdict['time'] #: str: The timestamp of when this Block was created
		self.bot = bot
	
	def delete(self):
		'''Removes block'''
		self.bot.unblock(self.user.id)

