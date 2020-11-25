class QBaseError(Exception):
	pass

class QHTTPException(QBaseError):
	def __init__(self, resp):
		message: str = resp.json()['error']
		super().__init__(message)