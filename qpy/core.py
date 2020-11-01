import requests

from .block import *
from .error import QHTTPException
from .favorite import *
from .feed import *
from .follow import *
from .notification import Notification
from .user import *
from .error import *


class Qpost:
	"""Represents the connection of the user to qpost

	Args:
		token (str): Token of said user

	"""
	def __init__(self, token: str):
		self.token = token

	def __request(self, endpoint: str, params: dict, method: str, datatype: str = 'json'):
		baseurl = 'https://qpostapp.com/api'
		auth = ' '.join(["Bearer", self.token])
		headers = {'Authorization': auth}
		resp = requests.request(method, baseurl+endpoint, **{datatype: params, 'headers': headers})
		if resp.status_code >= 400:
			raise QHTTPException(resp)
		return resp
	
	def get_badges(self):
		"""Get information for the badges in the top navigation bar for the current use

		Returns:
			dict
		"""
		endpoint= '/badgestatus'
		method = 'GET'
		resp = self.__request(endpoint, None, method, 'json')
		return resp.json()
	
	def __clear_badge(self, type_: str):
		"""Clears all unread items for a specific type"""
		endpoint = '/badgestatus'
		params = {'type': type_}
		method = 'DELETE'
		self.__request(endpoint, params, method, 'json')

	def clear_notifications(self):
		"""Clears all unread notifications"""
		self.__clear_badge('notifications')
	
	def clear_messages(self):
		"""Clears all unread messages"""
		self.__clear_badge('messages')
	
	def get_notifications(self, max_: int):
		"""Gets notifications for the user

		Returns:
			list[Notification]
		"""
		params = {'max': max_}
		endpoint = '/notifications'
		method = 'GET'
		resp = self.__request(endpoint, params, method, 'json')
		return [Notification(_, self) for _ in resp.json()]
	
	def _get_birthday(self, date):
		'''Gets birthdays of users followed by current user'''
		endpoint = '/birthdays'
		params = {'date': date}
		method = 'GET'
		self.__request(endpoint, params, method, 'json')

	def get_user(self, user: str):
		'''Gets a User object by their username
		
		Args:
			user (str): username of the user

		Returns:
			User
		'''
		endpoint = '/user'
		params = {'user': user}
		method = 'GET'
		resp = self.__request(endpoint, params, method, 'params')
		return User(resp.json(), self)
	
	def post_status(self, message: str, is_nsfw: bool = False, attachments: list = None, parent:int = None):
		'''Creates a new FeedEntry with either the type POST or REPLY, depending on whether the parent parameter is present
		
		Args:
			message (str): Content to be sent
			is_nsfw (bool, optional): A flag to mark your content as nsfw. Default to False
			attachments (list, optional): A list consisting of base64 strings (can be constructed with MediaBuilder)
			parent (int, optional): id of a status to be replied to
		
		Returns:
			:obj:`FeedEntry`
		'''
		endpoint = '/status'
		method = 'POST'
		params = {'message': message, 'nsfw': is_nsfw}
		if attachments is not None:
			params['attachments'] = attachments
		if parent is not None:
			params['parent'] = parent
		resp = self.__request(endpoint, params, method, 'json')
		return FeedEntry(resp.json(), self)
	
	def delete_status(self, id_: int):
		'''Deletes a specific FeedEntry by it's ID (type has to be POST or REPLY)
		
		Args:
			id_ (int): id of the status to be removed
		'''
		endpoint = '/status'
		params = {'id': id_}
		method = 'DELETE'
		self.__request(endpoint, params, method, 'json')
	
	def get_status(self, id_: int):
		'''Gets a specific FeedEntry by it's ID (type has to be POST or REPLY)
		
		Args:
			id_ (int): id of the status to get
		
		Returns:
			FeedEntry
		'''
		endpoint = '/status'
		params = {'id': id_}
		method = 'GET'
		resp = self.__request(endpoint, params, method, 'params')
		return FeedEntry(resp.json(), self)

	def block(self, targetid: int):
		'''Creates a new Block from the current user to a specific user
		
		Args:
			targetid (int): id of a User to be blocked
		'''
		endpoint = '/block'
		params = {'target': targetid}
		method = 'POST'
		resp = self.__request(endpoint, params, method, 'json')

	def unblock(self, targetid: int):
		'''Deletes a Block from the current user to a specific user
		
		Args:
			targeitd (id): id of a blocked User to be unblocked
		'''
		endpoint = '/block'
		params = {'target': targetid}
		method = 'DELETE'
		self.__request(endpoint, params, method, 'json')

	def get_block(self, targetid: int):
		'''Get information of a block created by the current user, targeting a specific user
		
		Returns:
			Block
		'''
		endpoint = '/block'
		params = {'target': targetid}
		method = 'GET'
		resp = self.__request(endpoint, params, method, 'params')
		return Block(resp.json(), self)

	def get_blocks(self, max_: int):
		'''Gets all blocked users for the current user
		
		Args:
			max_ (int): The maximum blocks to look for
		
		Returns:
			list[:obj:`Notification`]
		'''
		endpoint = '/blocks'
		params = {'max': max_}
		method = 'GET'
		resp = self.__request(endpoint, params, method, 'json')
		return [Block(_, self) for _ in resp.json()]

	def favorite(self, feedid):
		'''Creates a new Favorite from the current user to a specific FeedEntry
		
		Args:
			feedid (int): id of the status to be favorited
		
		Returns:
			Favorite
		'''
		endpoint = '/favorite'
		params = {'post': feedid}
		method = 'POST'
		resp = self.__request(endpoint, params, method, 'json')
		return Favorite(resp.json(), self)
	
	def unfavorite(self, feedid: int):
		'''Deletes a Favorite from the current user to a specific FeedEntry
		
		Args:
			feedid (int): The ID of the target FeedEntry
		'''
		endpoint = '/favorite'
		params = {'post': feedid}
		method = 'DELETE'
		self.__request(endpoint, params, method, 'json')

	def get_favorites(self, userid: int, max_: int):
		'''Gets all created favorites for a specific :obj:`User`
		
		Args:
			userid (int): The ID of the user to look for
			max_ (int): The maximum ID for favorites to look for
		
		Returns:
			list[:obj:`Favorite`]
		'''
		endpoint = '/favorites'
		params = {'user': userid, 'max': max_}
		method = 'GET'
		resp = self.__paramrequest(endpoint, params, method, 'json')
		return [Favorite(_, self) for _ in resp.json()]
	
	def get_feeds(self, userid: int, max_: int = None, min_: int = None, type_: str = 'posts'):
		'''Gets entries on a feed, by specific parameters
		
		Args:
			userid (int): The ID of the user to filter the feed entries by
			max_ (int): The maximum ID for feed entries to look for (can not be combined with min\_)
			min_ (int): The minimum ID for feed entries to look for (can not be combined with max\_)
			type_ (str, optional): The type of feed entries to load, either posts or replies, defaults to posts
		
		Returns:
			list[:obj:`FeedEntry`]
		'''
		if (max_ and min_):
			print("Can't set both max and min")
			return 
		endpoint = '/feed'
		params = {'max': max_, 'min': min_, 'user': userid, 'type': type_}
		method = 'GET'
		resp = self.__request(endpoint, params, method, 'json')
		return [FeedEntry(_, self) for _ in resp.json()]
	
	def get_follow(self, from_: int, to: int):
		'''Gets info about a specific follow relationship
		
		Args:
			from_ (int): The ID of the sending :obj:`User`
			to (int): The ID of the target :obj:`User`
		
		Returns:
			:obj:`Follow`
		'''
		endpoint = '/follow'
		params = {'from': from_, 'to': to}
		method = 'GET'
		resp = self.__request(endpoint, params, method, 'params')
		try:
			follow = Follow(resp.json(), self)
		except KeyError:
			follow = resp.json()
		return follow
	
	def get_follows(self, from_: int, to: int, max_: int = None):
		'''Gets all follow relationships for a specific user
		
		Args:
			from_ (int): The ID of the user to look for
			to (int): The ID of the user to look for
			max_ (int, optional): The maximum ID for follows to look for
		
		Returns:
			list[:obj:`Follow`]
		'''
		endpoint = '/follows'
		params = {'from': from_, 'to': to, 'max': max_}
		method = 'GET'
		resp = self.__request(endpoint, params, method, 'params')
		return [Follow(_, self) for _ in resp.json()]
	
	def follow(self, to: int):
		'''Creates a new Follow from the current user to a specific user
		
		Args:
			to (int): The ID of the target :obj:`User`
		'''
		endpoint = '/follow'
		params = {'to': to}
		method = 'POST'
		self.__request(endpoint, params, method, 'json')
	
	def unfollow(self, to: int):
		'''Deletes a follow relationship from the current user to a specific FeedEntry
		
		Args:
			to (int): The ID of the target :obj:`User`
		'''
		endpoint = '/follow'
		params = {'to': to}
		method = 'DELETE'
		resp = self.__request(endpoint, params, method, 'json')
	
	def known_followers(self, targetid: int, offset: int = None, limit: int = None):
		'''Gets all followers, the current user follows for the target user
		
		Args:
			targetid (int): The ID of the target user
			offset (int, optional): The amount of users to skip in the query
			limit (int, optional): The maximum amount of users to return
		
		Returns:
			list[:obj:`User`]
		'''
		endpoint = '/followersyouknow'
		params = {'target': targetid, 'offset': offset, 'limit': limit}
		method = 'GET'
		resp = self.__request(endpoint, params, method, 'params')
		return [User(_, self) for _ in resp.json()]
	
	def __follow_request_action(self, id_: int, action: str):
		'''Deletes a follow request and accepts or declines it'''
		if action not in ('accept', 'decline'):
			print("Invalid action")
			return
		endpoint = '/followRequest'
		params = {'id': id_, 'action': action}
		method = 'DELETE'
		resp = self.__request(endpoint, params, method, 'json')
	
	def accept_follow_request(self, id_: int):
		'''Accepts a follow request
		
		Args:
			id_ (int): The ID of the target FollowRequest
		'''
		self.__follow_request_action(id_, "accept")
	
	def decline_follow_request(self, id_: int):
		'''Declines a follow request
		
		Args:
			id_ (int): The ID of the target FollowRequest
		'''
		self.__follow_request_action(id_, "decline")
	
	def get_follow_requests(self, max_: int):
		'''Gets all open follow requests for a specific user
		
		Args:
			id_ (int): The maximum ID for follow requests to look for
		
		Returns:
			list[:obj:`FollowRequest`]
		'''
		endpoint = '/followRequest'
		params = {'max': max_}
		method = 'GET'
		resp = self.__request(endpoint, params, method, 'json')
		return [FollowRequest(_, self) for _ in resp.json()]
	
	def get_replies(self, feedid: int, page: int):
		'''Gets all replies to the specified status

		Args:
			feedid (int): The ID of the status to look for
			page: Used for pagination
		
		Returns:
			list[list[:obj:`Notification`]]
		'''
		endpoint = '/replies'
		params = {'feedEntry': feedid, 'page': page}
		method = 'GET'
		resp = self.__request(endpoint, params, method, 'params')
		batches = list()
		for batch in resp.json():
			replies = [Notification(_) for _ in batch]
			batches.append(replies)
		return batches
	
	def _search(self, type_: str, query: str, offset: int = None, limit: int = None):
		'''Searches for specific content on qpost'''
		endpoint = '/search'
		params = {'type': type_, 'query': query, 'offset': offset, 'limit': limit}
		method = 'GET'
		resp = self.__request(endpoint, params, method, 'params')
		return resp
	
	def search_users(self, query: str, offset: int = None, limit: int = None):
		'''Searches for specific users on qpost
		
		Args:
			query (str): The search query to use
			offset (int, optional): The offset to use for the query
			limit (int, optional): The maximum objects to return
		
		Returns:
			list[:obj:`User`]
		'''
		resp = self._search("user", query, offset, limit)
		return [User(_, self) for _ in resp.json()]
	
	def search_feeds(self, query: str, offset: int = None, limit: int = None):
		'''Searches for specific posts on qpost
		
		Args:
			query (str): The search query to use
			offset (int, optional): The offset to use for the query
			limit (int, optional): The maximum objects to return
		
		Returns:
			list[:obj:`FeedEntry`]
		'''
		resp = self._search("post", query, offset, limit)
		return [FeedEntry(_, self) for _ in resp.json()]

	def share(self, postid: int):
		'''Creates a new share from the current user to a specific FeedEntry
		
		Args:
			postid (int): The ID of the target FeedEntry
		
		Returns:
			:obj:`FeedEntry`
		'''
		endpoint = '/share'
		params = {'post': postid}
		method = 'POST'
		resp = self.__request(endpoint, params, method, 'json')
		return FeedEntry(resp.json(), self)

	def unshare(self, postid: int):
		'''Deletes a share from the current user to a specific FeedEntry
		
		Args:
			postid (int): The ID of the target FeedEntry (parent)
		'''
		endpoint = '/share'
		params = {'post': postid}
		method = 'DELETE'
		resp = self.__request(endpoint, params, method, 'json')

	def me(self):
		'''Gets the curent User object
		
		Returns:
			:obj:`User`
		'''
		endpoint = '/token/verify'
		method = 'POST'
		resp = self.__request(endpoint, None, method, 'json')
		return User(resp.json()['user'], self)
