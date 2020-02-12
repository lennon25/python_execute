#!/usr/bin/env python3

#类的方法
class people:
	# 定义基本属性
	name =""
	age = 0
	__weight = 0
	# 定义构造方法
	def __init__(self,n,a,w):
		self.name = n
		self.age = a
		self.__weight = w
	def speak(self):
		print(" %s 说：我 %d岁了。" %(self.name,self.age))


#实例化
p = people("Lennon",25, 60)
p.speak()


# 继承
class People:
	name = ''
	age = 0
	__weight = 0
	def __init__(self,n,a,w):
		self.name = n
		self.age = a
		self.__weight = w

	def speak(self):
		print("%s 说： 我 %是岁了。" %(self.name,self.age))


class Student(People):
	grade = ''
	def __init__(self,n,a,w,g):
		People.__init__(self,n,a,w)
		self.grade = g

	def speak(self):
		print("%s 说：我 %d 岁了, 我在读 %d 年级" % (self.name,self.age,self.grade))



s =Student("ken", 10, 60, 3)
s.speak()


# 多继承
class Speaker():
	topic = ''
	name = ''
	def __init__(self,n,t):
		self.name = n
		self.topic = t

	def speak(self):
		print("我叫 %s, 我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


class Sample(Speaker,Student):
    a =''
    def __init__(self,n,a,w,g,t):
        Student.__init__(self,n,a,w,g)
        Speaker.__init__(self,n,t)
 

test = Sample("Tim",25,80,4,"Python")
test.speak() 


#  方法重写
class Parent:
	def myMethod(self):
		print("调用父类方法")


class Child(Parent):
	def myMethod(self):
		print("调用子类方法")


c = Child()
c.myMethod()
super(Child,c).myMethod()



# 类的属性和方法
# 类的私有属性
class JustCounter:
	__secretCount = 0
	publicCount = 0

	def count(self):
		self.__secretCount += 1
		self.publicCount += 1
		print(self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
# print(counter.__secretCount) 私有属性


# 类的私有方法
class Site()
	def __init__(self, name, url):
		self.name = name
		self.__url = url

	def who(self):
		print("name ",self.name)
		print("url ", self.__url)

	def __foo(self):
		print("这是私有方法")

	def foo(self):
		print('这是共有方法')
		self.__foo()


x = Site("Lennon", "www.baidu.com")
x.who()
x.foo()
x.__foo()




