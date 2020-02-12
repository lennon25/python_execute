import asyncio
import threading
import time 


# 协程的生产者-消费者模型

# def consumer():
# 	r = ''
# 	while True:
# 		n = yield r
# 		if not n:
# 			return 
# 		print('[CONSUMER] Consuming %s...' % n)
# 		r = '200 OK'


# def produce(c):
# 	c.send(None)
# 	n = 0
# 	while n < 5:
# 		n = n + 1
# 		print('[PRODUCER] Producing %s...' % n)
# 		r = c.send(n)
# 		print('[PRODUCER] Consumer return: %s' % r)
# 	c.close()


# c = consumer()
# produce(c)


# 用asyncio实现hello world代码:
# @asyncio.coroutine
# def hello():
# 	print("Hello, World")
# 	# 异步调用
# 	r = yield from asyncio.sleep(1)
# 	print("Hello, again!")

# # 获取EventLoop:
# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
# loop.close()


# 封装task
# @asyncio.coroutine
# def hello_world():
# 	print("Hello, World! (%s)" % threading.currentThread())
# 	yield from asyncio.sleep(1)
# 	print("Hello, again! (%s)" % threading.currentThread())


# loop = asyncio.get_event_loop()
# tasks = [hello_world(), hello_world()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


@asyncio.coroutine
def wget(host):
	print("wget %s..." % host)
	connect = asyncio.open_connection(host, 80)
	reader, writer = yield from connect
	header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
	writer.write(header.encode('utf-8'))
	yield from writer.drain()
	while True:
		line =yield from reader.readline()
		if line == b'\r\n':
			break
		print("%s hader > %s" % (host, line.decode('utf-8').rstrip()))
	writer.close()


loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()



# async/await
# 协程在py3.5新的语法

async def hello():
	print("Hello, world!")
	r = await asyncio.sleep(1)
	print("Hello, again!")


async def hello(name):
	print("Hello, ", name)


# 协程的工作流
# coroutine = hello("world")
# loop = asyncio.get_event_loop()
# task = loop.create_task(coroutine)
# loop.run_until_complete(task)


# 回调函数
async def _sleep(x):
	time.sleep(2)
	return "sleep {}s".format(x)


def callback(future):
	print("This is a callback, get the return result: ", future.result())


coroutine = _sleep(2)
loop =asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)
# 添加回调哈数
task.add_done_callback(callback)
loop.run_until_complete(task)




