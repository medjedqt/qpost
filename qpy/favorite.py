from .feed import FeedEntry
from .user import User

class Favorite:
	def __init__(self, favdict: dict, bot):
		'''Represents qpost's Favorite object'''
		self.id = favdict['id']
		self.user = User(favdict['user'], bot)
		self.entry = FeedEntry(favdict['feedEntry'], bot)
		self.time_created = favdict['time']
		self.bot = bot
	
	def delete(self):
		self.bot.unfavorite(self.entry.id)

Favourite = Favorite
