class User:
	'''Represents a qpost User object'''
	def __init__(self, userdict: dict, bot):
		self.id = userdict['id'] #: int: The unique identifier of this user
		self.display_name = userdict['displayName'] #: str: The display name of this user
		self.username = userdict['username'] #: str: The username/"@-handle" of this user
		self.avatar_url = userdict['avatarURL'] #: str: The URL of this user's avatar
		self.header = userdict['header'] #: str: The URL of this user's header image
		self.bio = userdict['bio'] #: str: The biography of this user
		self.birthday = userdict['birthday'] #: str: The birthday date of this user in the format "Y-m-d"
		self.privacy_level = userdict['privacyLevel'] #: str: The privacy level of this user, one of these values; PUBLIC / PRIVATE / CLOSED
		self.time_created = userdict['time'] #: str: The timestamp of when this user was created
		self.is_verified = userdict['verified'] #: bool: Whether or not this user has a verified badge
		self.is_suspended = userdict['suspended'] #: bool: Whether or not this user's account was suspended
		self.total_posts = userdict['totalPostCount'] #: int: The total amount of feed entries this user has created
		self.total_following = userdict['followingCount'] #: int: The amount of users this user follows
		self.total_followers = userdict['followerCount'] #: int: The amount of users that follow this user
		self.total_favorites = userdict['favoritesCount'] #: int: The amount of posts this user has favorited
		self.follows_me = userdict['followsYou'] #: bool: Whether or not this user follows the currently authenticated user, false if not authenticated
		self.is_blocked = userdict['blocked'] #: bool: Whether or not the currently authenticated user has blocked this user, false if not authenticated
		self.extras = userdict['features'] #: list: Additional features that were enabled for this user
		self.identities = userdict['identities'] #: :obj:`LinkedAccount`: This user's linked identities
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
			offset (int, optional): The amount of users to skip in the query. Defaults to None.
			limit (int, optional): The maximum amount of users to return. Defaults to None.

		Returns:
			list[:obj:`User`]
		'''
		userlist = self.bot.known_followers(self.id, offset, limit)
		return userlist