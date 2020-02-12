#!/usr/bin/env python3

import time

def sleeptime(hour, min, sec):
	return hour*3600 + min*60 + sec

second = sleeptime(0,0,1)

for i in range(10):
	if i >= 0:
		print("e%s" % i)
		time.sleep(second)

	else:
		print("End")