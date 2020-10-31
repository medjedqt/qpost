
***
qpy
***

|pypi-build|

.. |pypi-build| image:: https://github.com/medjedqt/qpost/workflows/Upload%20Python%20Package/badge.svg

A basic python wrapper for `qpost <https://qpostapp.com>`_

Installing
##########

**Python 3.5 or higher is recommended**

.. code-block:: console

	# Linux/macOS
	python3 -m install pip install -U qpost

	# Windows
	py -3 -m pip install -U qpost


Example
#######

::

	from qpy import Qpost

	bot = Qpost("TOKEN")
	bot.post_status("Sent from Samsung Smart Fridge")

.. toctree::
	:maxdepth: 2
	
	intro
	examples
	qpost
	feed
	media
	user