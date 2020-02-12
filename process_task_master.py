#!/usr/bin/env python3

import random, time, queue
from multiprocessing.managers import BaseManager

# 创建task， result队列
task_queue = queue.Queue()
result_queue = queue.Queue()

# 从baseManager继承queueManager
class QueueManager(BaseManager):
	pass

# 把队列注册到网络上，callable关联queue对象
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)

# 绑定端口
manager = QueueManager(address=('', 5000), authkey=b'abc')
manager.start()

# 通过网络获的queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()

# 把任务放到task队列
for i in range(10):
	n = random.randint(0, 10000)
	print('Put task %d...' % n)
	task.put(n)

# 从result队列读取结果
print('Try get results...')
for i in range(10):
	r = result.get(timeout=10)
	print('Result: %s' % r)

# 关闭
manager.shutdown()
print('master exit.')
