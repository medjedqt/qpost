class User:
	'''Represents a qpost User object'''
	def __init__(self, userdict, bot):
		self.id: int = userdict['id'] #: The unique identifier of this user
		self.display_name: str = userdict['displayName'] #: The display name of this user
		self.username: str = userdict['username'] #: The username/"@-handle" of this user
		self.avatar_url: str = userdict['avatarURL'] #: The URL of this user's avatar
		self.header: str = userdict['header'] #: The URL of this user's header image
		self.bio: str = userdict['bio'] #: The biography of this user
		self.birthday: str = userdict['birthday'] #: The birthday date of this user in the format "Y-m-d"
		self.privacy_level: str = userdict['privacyLevel'] #: The privacy level of this user, one of these values; PUBLIC / PRIVATE / CLOSED
		self.time_created: str = userdict['time'] #: The timestamp of when this user was created
		self.is_verified: bool = userdict['verified'] #: Whether or not this user has a verified badge
		self.is_suspended: bool = userdict['suspended'] #: Whether or not this user's account was suspended
		self.total_posts: int = userdict['totalPostCount'] #: The total amount of feed entries this user has created
		self.total_following: int = userdict['followingCount'] #: The amount of users this user follows
		self.total_followers: int = userdict['followerCount'] #: The amount of users that follow this user
		self.total_favorites: int = userdict['favoritesCount'] #: The amount of posts this user has favorited
		self.follows_me: bool = userdict['followsYou'] #: Whether or not this user follows the currently authenticated user, false if not authenticated
		self.is_blocked: bool = userdict['blocked'] #: Whether or not the currently authenticated user has blocked this user, false if not authenticated
		self.extras: list = userdict['features'] #: Additional features that were enabled for this user
		self.identities: list[LinkedAccount] = [LinkedAccount(i) for i in userdict['identities']] #: This user's linked identities
		self.bot = bot

	def follow(self):
		'''Follows the user'''
		self.bot.follow(self.id)
	
	def unfollow(self):
		'''Unfollows the user'''
		self.bot.unfollow(self.id)
	
	def block(self):
		'''Blocks the user'''
		self.bot.block(self.id)
	
	def unblock(self):
		'''Unblocks the user'''
		self.bot.unblock(self.id)
	
	def known_followers(self, offset: int = None, limit: int = None):
		'''Returns a list of followers you know

		Args:
			offset : The amount of users to skip in the query.
			limit : The maximum amount of users to return.

		Returns:
			list[:obj:`User`]
		'''
		userlist: list[User] = self.bot.known_followers(self.id, offset, limit)
		return userlist

class LinkedAccount:
	def __init__(self, linkdict):
		'''Represents a qpost LinkedAccount object'''
		self.id: int = linkdict['id'] #: The unique identifier of this linked account
		self.service: str = linkdict['service'] #: The service that this linked account is a part of, one of these values; DISCORD / TWITCH / TWITTER / MASTODON / LASTFM / SPOTIFY / INSTAGRAM / REDDIT / YOUTUBE
		self.linked_user_id: str = linkdict['linkedUserId'] #: The id of this account in the third-party service's system
		self.linked_user_name: str = linkdict['linkedUserName'] #: The name of this account in the third-party service's system
		self.linked_user_avatar: str = linkdict['linkedUserAvatar'] #: The URL of this account's profile image
		self.time_created: str = linkdict['time'] #: The timestamp of when this account was created
		self.last_updated: str = linkdict['lastUpdate'] #: The timestamp of when this account was last updated