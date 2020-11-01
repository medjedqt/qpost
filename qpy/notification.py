from .feed import FeedEntry
from .follow import FollowRequest
from .user import User

class Notification:
	'''Represents qpost's Notification object'''
	def __init__(self, notifdict: dict, bot):
		self.id = notifdict['id'] #: int: The unique identifier of this Notification
		self.user = User(notifdict['user'], bot) #: :obj:`User`: The owner of this Notification
		self.type = notifdict['type'] #: str: The type of this Notification, one of these values; NEW_FOLLOWER / MENTION / FAVORITE / SHARE / REPLY / FOLLOW_REQUEST
		self.referenced_user = User(notifdict['referencedUser'], bot) if notifdict['referencedUser'] is not None else None #: :obj:`User`, optional: The User that was referenced in this notification
		self.referenced_feed = FeedEntry(notifdict['referencedFeedEntry'], bot) if notifdict['referencedFeedEntry'] is not None else None #: :obj:`FeedEntry`, optional: The FeedEntry that was referenced in this notification
		self.referenced_request = FollowRequest(notifdict['referencedFollowRequest'], bot) if notifdict['referencedFollowRequest'] is not None else None #: :obj:`FollowRequest`, optional: The FollowRequest that was referenced in this notification
		self.has_seen = notifdict['seen'] #: bool: Whether or not the user has seen this Notification
		self.notified = notifdict['notified'] #: bool: Whether or not the user has been notified about this Notification
		self.time_created = notifdict['time'] #: str: The timestamp of when this Notification was created