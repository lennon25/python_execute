
def mytest():
	pass

class People():

	def jump(self):
		print("jumping...")

	@staticmethod
	def speak(self):
		print("speaking...")

	@classmethod
	def run(cls):
		print("running...")


print(type(mytest))
print("===========")

p = People()

print(type(p.jump))
print(type(People.jump))
print("=============")

print(type(p.speak))
print(type(People.speak))
print("==============")


print(type(p.run))
print(type(People.run))
print("==============")
