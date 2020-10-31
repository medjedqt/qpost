Examples
--------

A basic implementation of qpy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

	import qpy

	bot = qpy.Qpost("TOKEN")
	bot.post_status("I'm in")

Sending an image
^^^^^^^^^^^^^^^^

::

	import qpy

	bot = qpy.Qpost("TOKEN")
	media = qpy.MediaBuilder()
	media.add(r"your/path/to/image.png")
	bot.post_status(message = "This is an image post", attachments = media.medias)

Following a User
^^^^^^^^^^^^^^^^

::

	import qpy

	bot = qpy.Qpost("TOKEN")
	user = bot.get_user("Zeryther")
	user.follow()