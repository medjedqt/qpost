
from .user import User
import base64

class FeedEntry:
	'''Represents qpost's FeedEntry object'''
	def __init__(self, feeddict: dict, bot):
		self.id = feeddict['id'] #: int: The unique identifier of this :obj:`FeedEntry`
		self.user = User(feeddict['user'], bot) #: :obj:`User`: The creator of this :obj:`FeedEntry`
		self.text = feeddict['text'] #: str: The message of this :obj:`FeedEntry`
		self.parent = FeedEntry(feeddict['parent'], bot) if feeddict['parent'] is not None else None #: :obj:`FeedEntry`: The parent of this :obj:`FeedEntry` (only for types REPLY and SHARE)
		self.type = feeddict['type'] #: str: The type of this :obj:`FeedEntry`, one of these values: POST / REPLY / NEW_FOLLOWING / SHARE
		self.is_nsfw = feeddict['nsfw'] #: bool: Whether or not this :obj:`FeedEntry` was marked as 18+
		self.attachments = [MediaFile(_) for _ in feeddict['attachments']] if feeddict['attachments'] is not None else None #: :obj:`MediaFile`: The attachments of this :obj:`FeedEntry`
		self.time_created = feeddict['time'] #: str: The timestamp of when this :obj:`FeedEntry` was created
		self.total_replies = feeddict['replyCount'] #: int: The amount of replies this :obj:`FeedEntry` has
		self.total_shares = feeddict['shareCount'] #: int: The amount of shares this :obj:`FeedEntry` has
		self.total_favorites = feeddict['favoriteCount'] #: int: The amount of favorites this :obj:`FeedEntry` has
		self.has_shared = feeddict['shared'] #: bool: Whether or not the currently authenticated user has shared this :obj:`FeedEntry`, false if not authenticated
		self.has_favorited = feeddict['favorited'] #: bool: Whether or not the currently authenticated user has favorited this :obj:`FeedEntry`, false if not authenticated
		self.bot = bot
	
	def delete(self):
		'''Deletes this :obj:`FeedEntry`'''
		self.bot.delete_status(self.id)
	
	def favorite(self):
		'''Favorites this :obj:`FeedEntry`
		
		Returns:
			:obj:`Favorite`
		'''
		return self.bot.favorite(self.id)
	
	def unfavorite(self):
		'''Unfavorites this :obj:`FeedEntry`'''
		self.bot.unfavorite(self.id)
	
	def share(self):
		'''Shares this :obj:`FeedEntry`
		
		Returns:
			:obj:`FeedEntry`
		'''
		return self.bot.share(self.id)
	
	def unshare(self):
		'''Unshares this :obj:`FeedEntry`'''
		self.bot.unshare(self.id)

class MediaFile:
	'''Represents qpost's MediaFile object

	Args:
		mediadict (dict): Media data
	'''
	def __init__(self, mediadict: dict):
		self.id = mediadict['id'] #: int: The unique identifier of this :obj:`MediaFile`
		self.sha256 = mediadict['sha256'] #: str: The sha256 hash of this :obj:`MediaFile`
		self.url = mediadict['url'] #: str: The URL of this :obj:`MediaFile`
		self.type = mediadict['type'] #: str: The type of this :obj:`MediaFile`, one of these values; IMAGE / VIDEO / LINK
		self.time_created = mediadict['time'] #: str: The timestamp of when this :obj:`MediaFile` was created

class MediaBuilder:
	'''A utility class to help you turn image files into base64 string lists'''
	def __init__(self):
		self.medias = list() #: list: List of medias to be sent

	def add(self, imgpath: str):
		'''Converts an image file into base64 and appends it to a list ready to be sent

		Args:
			imgpath (str): Path to the image file
		'''
		with open(imgpath, 'rb') as imgfile:
			encoded_string = base64.b64encode(imgfile.read()).decode('utf-8')
		self.medias.append(encoded_string)