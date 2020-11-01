from .feed import FeedEntry
from .user import User

class Favorite:
	'''Represents qpost's Favorite object'''
	def __init__(self, favdict: dict, bot):
		self.id = favdict['id'] #: int: The unique identifier of this Favorite
		self.user = User(favdict['user'], bot) #: :obj:`User`: The creator of this Favorite
		self.entry = FeedEntry(favdict['feedEntry'], bot) #: :obj:`FeedEntry`: The FeedEntry that was favorited
		self.time_created = favdict['time'] #: str: The timestamp of when this Favorite was created
		self.bot = bot
	
	def delete(self):
		'''Removes favorite'''
		self.bot.unfavorite(self.entry.id)
