from .feed import FeedEntry
from .user import User

class Favorite:
	'''Represents qpost's Favorite object'''
	def __init__(self, favdict, bot):
		self.id: int = favdict['id'] #: The unique identifier of this Favorite
		self.user: User = User(favdict['user'], bot) #: The creator of this Favorite
		self.entry: FeedEntry = FeedEntry(favdict['feedEntry'], bot) #: The FeedEntry that was favorited
		self.time_created: str = favdict['time'] #: The timestamp of when this Favorite was created
		self.bot = bot
	
	def delete(self):
		'''Removes favorite'''
		self.bot.unfavorite(self.entry.id)
