class User:
	def __init__(self, userdict: dict, bot):
		'''Represents a qpost User object'''
		self.id = userdict['id']
		self.display_name = userdict['displayName']
		self.username = userdict['username']
		self.avatar_url = userdict['avatarURL']
		self.header = userdict['header']
		self.bio = userdict['bio']
		self.birthday = userdict['birthday']
		self.privacy_level = userdict['privacyLevel']
		self.time_created = userdict['time']
		self.is_verified = userdict['verified']
		self.is_suspended = userdict['suspended']
		self.total_posts = userdict['totalPostCount']
		self.total_following = userdict['followingCount']
		self.total_followers = userdict['followerCount']
		self.total_favorites = userdict['favoritesCount']
		self.total_favourites = self.total_favorites
		self.follows_me = userdict['followsYou']
		self.is_blocked = userdict['blocked']
		self.extras = userdict['features']
		self.identities = userdict['identities']
		self.bot = bot

	def follow(self):
		self.bot.follow(self.id)
	
	def unfollow(self):
		self.bot.unfollow(self.id)
	
	def block(self):
		self.bot.block(self.id)
	
	def unblock(self):
		self.bot.unblock(self.id)
	
	def known_followers(self, offset: int = None, limit: int = None):
		userlist = self.bot.known_followers(self.id, offset, limit)
		return userlist