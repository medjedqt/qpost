from .feed import FeedEntry
from .follow import FollowRequest
from .user import User

class Notification:
	'''Represents qpost's Notification object'''
	def __init__(self, notifdict, bot):
		self.id: int = notifdict['id'] #: The unique identifier of this Notification
		self.user: User = User(notifdict['user'], bot) #: The owner of this Notification
		self.type: str = notifdict['type'] #: The type of this Notification, one of these values; NEW_FOLLOWER / MENTION / FAVORITE / SHARE / REPLY / FOLLOW_REQUEST
		self.referenced_user: User = User(notifdict['referencedUser'], bot) if notifdict['referencedUser'] is not None else None #: The User that was referenced in this notification
		self.referenced_feed: User = FeedEntry(notifdict['referencedFeedEntry'], bot) if notifdict['referencedFeedEntry'] is not None else None #: The FeedEntry that was referenced in this notification
		self.referenced_request: FollowRequest = FollowRequest(notifdict['referencedFollowRequest'], bot) if notifdict['referencedFollowRequest'] is not None else None #: The FollowRequest that was referenced in this notification
		self.has_seen: bool = notifdict['seen'] #: Whether or not the user has seen this Notification
		self.notified: bool = notifdict['notified'] #: Whether or not the user has been notified about this Notification
		self.time_created: str = notifdict['time'] #: The timestamp of when this Notification was created
