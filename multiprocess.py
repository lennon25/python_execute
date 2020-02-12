#!/usr/bin/env python3


from multiprocessing import Process, Pool, Queue
import os, time, random


# fork()调用，父进程启动子进程处理新任务
# print('Process (%s) start...' % os.getpid())

# pid = os.fork()
# if pid == 0:
# 	print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
# 	print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


# multiprocessing

# def run_proc(name):
# 	print('Run child process %s (%s)...' % (name, os.getpid()))

# if __name__ =='__main__':
# 	print('Parent process %s.' % os.getpid())
# 	p = Process(target=run_proc, args=('test',))
# 	print('Child process will start.')
# 	p.start()
# 	p.join()
# 	print('Child process end.')



# Pool 进程池

def long_time_task(name):
	print('Run task %s (%s)...' % (name, os.getpid()))
	start = time.time()
	time.sleep(random.random() * 3)
	end = time.time()
	print('Task %s runs %0.2f seconds.' % (name, end-start))


if __name__ == '__main__':
	print('Parent process %s.' % os.getpid())
	p = Pool(3)  # pool设置同时运行Run进程大小
	for i in range(5):
		p.apply_async(long_time_task, args=(i,))
	print('Waiting for all subprocesses done')
	p.close()
	p.join()
	print('All subprocesses done.')


# 进程间通信
# 在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：
# 写数据进程执行代码
def write(q):
	print('Process to write: %s ' % os.getpid())
	for value in ['A', 'B', 'C']:
		print('Put %s to queue...' % value)
		q.put(value)
		time.sleep(random.random())

# 读数据的进程执行代码
def read(q):
	print('Process to read: %s' % os.getpid())
	while True:
		value = q.get(True)
		print('Get %s from queue.' % value)


if __name__ == '__main__':
	# 父进程创建Queue, 并传给子进程
	q = Queue()
	pw = Process(target=write, args=(q,))
	pr = Process(target=read, args=(q,))
	pw.start()
	pr.start()
	pw.join()
	pr.terminate()  # 强制结束pr
