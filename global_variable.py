import unittest

class TestGlobalVariable(unittest.TestCase):

#	global y
	y = 0

	def test_1(self):
		global y
		y = 2
		print("5",y)

	def test_2(self):
	#	global y
		sum = y + 2
		print("3",sum)

	@unittest.skipIf(y ==2, "skip case") 	
	def test_3(self):
	#	# global y
		print("2",y)

	print("step x")
	print(y)


if __name__ == "__main__":
	suite = unittest.TestSuite()
	suite.addTest(TestGlobalVariable("test_1"))
	suite.addTest(TestGlobalVariable("test_2"))
	suite.addTest(TestGlobalVariable("test_3"))
	unittest.run(suite)

x = 0

def a():
	global x
	x = 2

print(x)
a()
print(x)

