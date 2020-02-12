class Error(Exception):
	pass

class InputError(Error):
	
	def __init__(self, expression, message):
		self.expression = expression
		self.message = message

class TransitionError(Error):

	def __init_(self, previous, next, message):
		self.previous = previous
		self.next = next
		self.message =message

