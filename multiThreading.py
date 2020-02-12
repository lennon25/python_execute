#!/usr/bin/env python3

import time, threading

# threading
# 启动一个线程就是把一个函数传入并创建Thread实例,调用start()执行
def loop():
	print('Thread %s is runing...' % threading.current_thread().name)
	n = 0
	while n < 5:
		n = n + 1
		print('Thread %s >>> %s' % (threading.current_thread().name, n))
		time.sleep(1)
	print('Thread %s ended.' % threading.current_thread().name)


print('Thread %s is runing...' % threading.current_thread().name)
t = threading.Thread(target=loop, name = 'LoopThread')
t.start()
t.join()
print('Thread %s ended.' % threading.current_thread().name)


# threading lock
balance = 0
lock = threading.Lock()

def change_it(n):
	global balance
	balance = balance + n
	balance = balance - n

def run_thread(n):
	for i in range(1000):
		# 获取thread lock
		lock.acquire()
		try:
			change_it(n)
		finally:
			lock.release()


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)


# ThreadLocal
# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
	std = local_school.student
	print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
	local_school.student = name
	process_student()


t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name= 'Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()





