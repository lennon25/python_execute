#!/usr/bin/env python3

class Student(object):
	def get_score(self):
		return self._socre

	def set_score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an interger!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0-100.')
		self._socre = value
		

class Student():
	def __init__(self, name, gender):
		self.__name = name
		self.__gender = gender

	def get_gender(self):
		return self.__gender

	def set_gender(self, gender):
		if gender == 'male' or 'female':
			self.__gender = gender
		else:
			raise ValueError("Bad value.")



bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')