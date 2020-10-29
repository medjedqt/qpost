
from .user import User
import base64

class FeedEntry:
	def __init__(self, feeddict: dict, bot):
		'''Represents qpost's FeedEntry object'''
		self.id = feeddict['id']
		self.user = User(feeddict['user'], bot)
		self.text = feeddict['text']
		self.parent = FeedEntry(feeddict['parent'], bot) if feeddict['parent'] is not None else None
		self.type = feeddict['type']
		self.is_nsfw = feeddict['nsfw']
		self.attachments = [MediaFile(_) for _ in feeddict['attachments']] if feeddict['attachments'] is not None else None
		self.time_created = feeddict['time']
		self.total_replies = feeddict['replyCount']
		self.total_shares = feeddict['shareCount']
		self.total_favorites = feeddict['favoriteCount']
		self.has_shared = feeddict['shared']
		self.has_favorited = feeddict['favorited']
		self.bot = bot
	
	def delete(self):
		self.bot.delete_status(self.id)
	
	def favorite(self):
		return self.bot.favorite(self.id)
	
	def unfavorite(self):
		self.bot.unfavorite(self.id)
	
	def share(self):
		return self.bot.share(self.id)
	
	def unshare(self):
		self.bot.unshare(self.id)

class MediaFile:
	def __init__(self, mediadict: dict):
		'''Represents qpost's MediaFile object'''
		self.id = mediadict['id']
		self.sha256 = mediadict['sha256']
		self.url = mediadict['url']
		self.type = mediadict['type']
		self.time_created = mediadict['time']

class MediaBuilder:
	def __init__(self):
		self.medias = list()

	def add(self, imgpath: str):
		with open(imgpath, 'rb') as imgfile:
			encoded_string = base64.b64encode(imgfile.read()).decode('utf-8')
		self.medias.append(encoded_string)
	
	def get(self):
		return self.medias