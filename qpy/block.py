from .core import Qpost
from .user import User

class Block:
	def __init__(self, blockdict: dict, bot: Qpost):
		'''Represents qpost's Block object'''
		self.id = blockdict['id']
		self.user = User(blockdict['user'])
		self.target = User(blockdict['target'])
		self.time_created = blockdict['time']
		self.bot = bot
	
	def delete(self):
		self.bot.unblock(self.user.id)

