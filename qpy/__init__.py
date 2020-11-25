"""
qpost API Wrapper
~~~~~~~~~~~~~~~~~

A basic wrapper for the qpost API.

"""

__title__ = 'qpost'
__author__ = 'medjed'
__version__ = '0.0.1'

from .block import Block
from .core import Qpost
from .favorite import Favorite
from .feed import FeedEntry, MediaFile, MediaBuilder
from .follow import Follow, FollowRequest
from .notification import Notification
from .user import User, LinkedAccount