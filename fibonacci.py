#!/usr/bin/env python3

import sys

def fibonacci(n):  # 生成器函数 -斐波那契
	a, b, counter = 0, 1, 0
	while True:
		if (counter > n):
			return
		yield a
		a, b = b, a + b
		counter += 1


f = fibonacci(10)	# f是一个迭代器，由生成器返回生成

while True:
	try:
		print(next(f), end= " ")
	except StopIteration:
		sys.exit()



#  __iter__ 定制类，该返回迭代对象

class Fib(object):
	def __init__(self):
		self.a self.b = 0, 1

	def __iter__(self):
		return self

	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > 10000:
			raise StopIteration
		return self.a


for n in Fib():
	print(n)

