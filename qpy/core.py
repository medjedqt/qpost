import json
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
	def __init__(self, token: str):
		"""
		Represents the connection of the user to qpost
		```
		Attributes
		~~~~~~~~~~
		token : str
		- Token of said user
		"""
		self.token = token
		self.me = self.__me()

	def __request(self, endpoint: str, params: dict, method: str):
		baseurl = 'https://qpostapp.com/api'
		auth = ' '.join(["Bearer", self.token])
		headers = {'Authorization': auth}
		resp = requests.request(method, baseurl+endpoint, json=params, headers=headers)
		if resp.status_code >= 400:
			raise QHTTPException(resp)
		return resp

	def __paramrequest(self, endpoint: str, params: dict, method: str):
		baseurl = 'https://qpostapp.com/api'
		auth = ' '.join(["Bearer", self.token])
		headers = {'Authorization': auth}
		resp = requests.request(method, baseurl+endpoint, params=params, headers=headers)
		if resp.status_code >= 400:
			raise QHTTPException(resp)
		return resp
	
	def get_badge(self):
		'''Get information for the badges in the top navigation bar for the current user'''
		endpoint= '/badgestatus'
		method = 'GET'
		resp = self.__request(endpoint, None, method)
		return resp.json()
	
	def clear_badge(self, type_: str):
		'''Clears all unread items for a specific type'''
		endpoint = '/badgestatus'
		params = {'type': type_}
		method = 'DELETE'
		resp = self.__request(endpoint, params, method)

	def clear_notifications(self):
		'''Clears all unread notifications'''
		self.clear_badge('notifications')
	
	def clear_messages(self):
		'''Clears all unread messages'''
		self.clear_badge('messages')
	
	def get_notifications(self, max_: int):
		'''Gets notification for the user'''
		params = {'max': max_}
		endpoint = '/notifications'
		method = 'GET'
		resp = self.__request(endpoint, params, method)
		return [Notification(_) for _ in resp.json()]
	
	def get_birthday(self, date):
		'''Gets birthdays of users followed by current user'''
		endpoint = '/birthdays'
		params = {'date': date}
		method = 'GET'
		self.__request(endpoint, params, method)

	def get_user(self, user: str):
		'''Gets a User object by their username'''
		endpoint = '/user'
		params = {'user': user}
		method = 'GET'
		resp = self.__paramrequest(endpoint, params, method)
		return User(resp.json(), self)
	
	def post_status(self, message: str, nsfw: bool = False, attachments: list = None, parent: int = None):
		'''Creates a new FeedEntry with either the type POST or REPLY, depending on whether the parent parameter is present'''
		endpoint = '/status'
		params = {'message': message, 'nsfw': nsfw}
		method = 'POST'
		resp = self.__request(endpoint, params, method)
		return resp.json()
	
	def delete_status(self, id_: int):
		'''Deletes a specific FeedEntry by it's ID (type has to be POST or REPLY)'''
		endpoint = '/status'
		params = {'id': id_}
		method = 'DELETE'
		resp = self.__request(endpoint, params, method)
	
	def get_status(self, id_: int):
		'''Gets a specific FeedEntry by it's ID (type has to be POST or REPLY)'''
		endpoint = '/status'
		params = {'id': id_}
		method = 'GET'
		resp = self.__request(endpoint, params, method)
		return FeedEntry(resp.json(), self)

	def block(self, targetid):
		'''Creates a new Block from the current user to a specific user'''
		endpoint = '/block'
		params = {'target': targetid}
		method = 'POST'
		resp = self.__request(endpoint, params, method)

	def unblock(self, targetid: int):
		'''Deletes a Block from the current user to a specific user'''
		endpoint = '/block'
		params = {'target': targetid}
		method = 'DELETE'
		resp = self.__request(endpoint, params, method)

	def get_block(self, targetid: int):
		'''Get information of a block created by the current user, targeting a specific user'''
		endpoint = '/block'
		params = {'target': targetid}
		method = 'GET'
		resp = self.__paramrequest(endpoint, params, method)
		return Block(resp.json(), self)

	def get_blocks(self, max_: int):
		'''Gets all blocked users for the current user'''
		endpoint = '/blocks'
		params = {'max': max_}
		method = 'GET'
		resp = self.__request(endpoint, params, method)
		return [Block(_, self) for _ in resp.json()]

	def favorite(self, feedid):
		'''Creates a new Favorite from the current user to a specific FeedEntry'''
		endpoint = '/favorite'
		params = {'post': feedid}
		method = 'POST'
		resp = self.__request(endpoint, params, method)
		return Favorite(resp.json(), self)
	
	def unfavorite(self, feedid):
		'''Deletes a Favorite from the current user to a specific FeedEntry'''
		endpoint = '/favorite'
		params = {'post': feedid}
		method = 'DELETE'
		resp = self.__request(endpoint, params, method)

	def get_favorites(self, userid: int, max_: int):
		'''Gets all created favorites for a specific User'''
		endpoint = '/favorites'
		params = {'user': userid, 'max': max_}
		method = 'GET'
		resp = self.__paramrequest(endpoint, params, method)
		return [Favorite(_, self) for _ in resp.json()]
	
	def get_feed(self, userid, max_ = None, min_ = None, type_ = 'posts'):
		'''Gets entries on a feed, by specific parameters'''
		if (max_ and min_):
			print("Can't set both max and min")
			return 
		endpoint = '/feed'
		params = {'max': max_, 'min': min_, 'user': userid, 'type': type_}
		method = 'GET'
		resp = self.__request(endpoint, params, method)
		return [FeedEntry(_, self) for _ in resp.json()]
	
	def get_follow(self, from_, to):
		'''Gets info about a specific follow relationship'''
		endpoint = '/follow'
		params = {'from': from_, 'to': to}
		method = 'GET'
		resp = self.__request(endpoint, params, method)
		try:
			follow = Follow(resp.json(), self)
		except KeyError:
			follow = resp.json()
	
	def get_follows(self, from_, to, max_ = None):
		'''Gets all follow relationships for a specific user'''
		endpoint = '/follows'
		params = {'from': from_, 'to': to, 'max': max_}
		method = 'GET'
		resp = self.__paramrequest(endpoint, params, method)
		return [Follow(_, self) for _ in resp.json()]
	
	def follow(self, to):
		'''Creates a new Follow from the current user to a specific user'''
		endpoint = '/follow'
		params = {'to': to}
		method = 'POST'
		resp = self.__request(endpoint, params, method)
		return resp.json()['status']
	
	def unfollow(self, to):
		'''Deletes a follow relationship from the current user to a specific FeedEntry'''
		endpoint = '/follower'
		params = {'to': to}
		method = 'DELETE'
		resp = self.__request(endpoint, params, method)
		return resp.json()['status']
	
	def known_followers(self, targetid, offset = None, limit = None):
		'''Gets all followers, the current user follows for the target user'''
		endpoint = '/followersyouknow'
		params = {'target': targetid, 'offset': offset, 'limit': limit}
		method = 'GET'
		resp = self.__paramrequest(endpoint, params, method)
		return [User(_, self) for _ in resp.json()]
	
	def __follow_request_action(self, id_: int, action: str):
		'''Deletes a follow request and accepts or declines it'''
		if action not in ('accept', 'decline'):
			print("Invalid action")
			return
		endpoint = '/followRequest'
		params = {'id': id_, 'action': action}
		method = 'DELETE'
		resp = self.__request(endpoint, params, method)
	
	def accept_follow_request(self, id_: int):
		'''Accepts a follow request'''
		self.__follow_request_action(id_, "accept")
	
	def decline_follow_request(self, id_: int):
		'''Declines a follow request'''
		self.__follow_request_action(id_, "decline")
	
	def get_follow_requests(self, max_: int):
		'''Gets all open follow requests for a specific user'''
		endpoint = '/followRequest'
		params = {'max': max_}
		method = 'GET'
		resp = self.__request(endpoint, params, method)
		return [FollowRequest(_, self) for _ in resp.json()]
	
	def get_replies(self, feedid: int, page: int):
		'''Gets all replies to the specified status'''
		endpoint = '/replies'
		params = {'feedEntry': feedid, 'page': page}
		method = 'GET'
		resp = self.__paramrequest(endpoint, params, method)
		batches = list()
		for batch in resp.json():
			replies = [Notification(_) for _ in batch]
			batches.append(replies)
		return batches
	
	def search(self, type_: str, query: str, offset: int = None, limit: int = None):
		'''Searches for specific content on qpost'''
		endpoint = '/search'
		params = {'type': type_, 'query': query, 'offset': offset, 'limit': limit}
		method = 'GET'
		resp = self.__paramrequest(endpoint, params, method)
		return resp
	
	def search_users(self, query: str, offset: int = None, limit: int = None):
		'''Searches for specific users on qpost'''
		resp = self.search("user", query, offset, limit)
		return [User(_, self) for _ in resp.json()]
	
	def search_feed(self, query: str, offset: int = None, limit: int = None):
		'''Searches for specific posts on qpost'''
		resp = self.search("post", query, offset, limit)
		return [FeedEntry(_, self) for _ in resp.json()]

	def share(self, postid):
		'''Creates a new share from the current user to a specific FeedEntry'''
		endpoint = '/share'
		params = {'post': postid}
		method = 'POST'
		resp = self.__request(endpoint, params, method)
		return FeedEntry(self.json(), self)

	def unshare(self, postid):
		'''Deletes a share from the current user to a specific FeedEntry'''
		endpoint = '/share'
		params = {'post': postid}
		method = 'DELETE'
		resp = self.__request(endpoint, params, method)
		return FeedEntry(resp.json(), self)

	def __me(self):
		'''Gets the curent User object'''
		endpoint = '/token/verify'
		method = 'POST'
		resp = self.__request(endpoint, None, method)
		return User(resp.json()['user'], self)
