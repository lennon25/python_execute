
"""@property 装饰器负责将方法变成属性调用"""

class Student(object):

	@property
	def score(self):
		return self._score

	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0-100')
		self._score = value

s = Student()
s.score = 60
s.score
# s.score = 9999


class Screen():
	@property 
	def width(self):
		return self._width

	@width.setter
	def width(self, width):
		self._width = width

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self, height):
		self._height = height

	@property
	def resolution(self):
		return self._height * self._width



s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
if s.resolution == 786432:
	print('pass')
else:
	print('fail')
	

		