
import itertools

def pi(n):
	natuals = itertools.count(1,2)
	ns = itertools.takewhile(lambda x: x <=2*n-1, natuals)
	index = -1
	sum = 0
	for i in ns:
		index *= -1
		sum += index*4/i
	return sum



print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')