#!/usr/bin/env python3

import threading, multiprocessing

# 死循环

def loop():
	x = 0
	while True:
		x = x ^ 1

for i in range(multiprocessing.cpu_count()):
	t = threading.Thread(target=loop)
	t.start()