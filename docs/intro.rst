.. currentmodule:: qpy

############
Introduction
############

Getting a User Token
====================

In order to work with the library and the qpost API, we'll need to;

#. Log into `qpost <https://qpostapp.com>`_.
#. Turn on developer mode/inspect element/skid mode.
#. Head to the ``Application`` tab.
#. Find ``qpoststoredtoken`` and copy its contents.
#. Remove the surrounding ``[]``\ s and ``%22``\ s

Examples
========

A basic implementation of qpy
-----------------------------

::

	import qpy

	bot = qpy.Qpost("TOKEN")
	bot.post_status("I'm in")

Sending an image
----------------

::

	import qpy

	bot = qpy.Qpost("TOKEN")
	media = qpy.MediaBuilder()
	media.add(r"your/path/to/image.png")
	bot.post_status(message = "This is an image post", attachments = media.medias)

Following a User
----------------

::

	import qpy

	bot = qpy.Qpost("TOKEN")
	user = bot.get_user("Zeryther")
	user.follow()