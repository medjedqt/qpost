from .feed import FeedEntry
from .follow import FollowRequest
from .user import User

class Notification:
	def __init__(self, notifdict: dict, bot):
		'''Represents qpost's Notification object'''
		self.id = notifdict['id']
		self.user = User(notifdict['user'], bot)
		self.type = notifdict['type']
		self.referenced_user = User(notifdict['referencedUser'], bot) if notifdict['referencedUser'] is not None else None
		self.referenced_feed = FeedEntry(notifdict['referencedFeedEntry'], bot) if notifdict['referencedFeedEntry'] is not None else None
		self.referenced_request = FollowRequest(notifdict['referencedFollowRequest'], bot) if notifdict['referencedFollowRequest'] is not None else None
		self.has_seen = notifdict['seen']
		self.notified = notifdict['notified']
		self.time_created = notifdict['time']