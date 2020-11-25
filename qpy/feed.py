from .user import User
import base64

class FeedEntry:
	'''Represents qpost's FeedEntry object'''
	def __init__(self, feeddict, bot):
		self.id: int = feeddict['id'] #: The unique identifier of this :obj:`FeedEntry`
		self.user: User = User(feeddict['user'], bot) #: The creator of this :obj:`FeedEntry`
		self.text: str = feeddict['text'] #: The message of this :obj:`FeedEntry`
		self.parent: FeedEntry = FeedEntry(feeddict['parent'], bot) if feeddict['parent'] is not None else None #: The parent of this :obj:`FeedEntry` (only for types REPLY and SHARE)
		self.type: str = feeddict['type'] #: The type of this :obj:`FeedEntry`, one of these values: POST / REPLY / NEW_FOLLOWING / SHARE
		self.is_nsfw: bool = feeddict['nsfw'] #: Whether or not this :obj:`FeedEntry` was marked as 18+
		self.attachments: list[MediaFile] = [MediaFile(_) for _ in feeddict['attachments']] if feeddict['attachments'] is not None else None #: The attachments of this :obj:`FeedEntry`
		self.time_created: str = feeddict['time'] #: The timestamp of when this :obj:`FeedEntry` was created
		self.total_replies: int = feeddict['replyCount'] #: The amount of replies this :obj:`FeedEntry` has
		self.total_shares: int = feeddict['shareCount'] #: The amount of shares this :obj:`FeedEntry` has
		self.total_favorites: int = feeddict['favoriteCount'] #: The amount of favorites this :obj:`FeedEntry` has
		self.has_shared: bool = feeddict['shared'] #: Whether or not the currently authenticated user has shared this :obj:`FeedEntry`, false if not authenticated
		self.has_favorited: bool = feeddict['favorited'] #: Whether or not the currently authenticated user has favorited this :obj:`FeedEntry`, false if not authenticated
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
	'''Represents qpost's MediaFile object'''
	def __init__(self, mediadict):
		self.id: int = mediadict['id'] #: The unique identifier of this :obj:`MediaFile`
		self.sha256: str = mediadict['sha256'] #: The sha256 hash of this :obj:`MediaFile`
		self.url: str = mediadict['url'] #: The URL of this :obj:`MediaFile`
		self.type: str = mediadict['type'] #: The type of this :obj:`MediaFile`, one of these values; IMAGE / VIDEO / LINK
		self.time_created: str = mediadict['time'] #: The timestamp of when this :obj:`MediaFile` was created

class MediaBuilder:
	'''A utility class to help you turn image files into base64 string lists'''
	def __init__(self):
		self.medias: list[str] = list() #: List of medias to be sent

	def add(self, imgpath: str):
		'''Converts an image file into base64 and appends it to a list ready to be sent

		Args:
			imgpath: Path to the image file
		'''
		with open(imgpath, 'rb') as imgfile:
			encoded_string = base64.b64encode(imgfile.read()).decode('utf-8')
		self.medias.append(encoded_string)
		return self