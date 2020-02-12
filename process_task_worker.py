#!/usr/bin/env python3

import time, sys, queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
	pass

# 从网络上获取Queue, 注册时提供名字
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
m.connect()

# 获取Queue的对象
task = m.get_task_queue()
result = m.get_result_queue()

# 从task队列中取任务，并把结果写入result队列：
for i in range(10):
	try:
		n = task.get(timeout=1)
		print('run task %d * %d...' % (n,n))
		r = '%d * %d = %d' % (n, n, n*n)
		time.sleep(1)
		result.put(r)
	except Queue.Empty:
		print('task queue is empty.')

print('Worker exit.')
