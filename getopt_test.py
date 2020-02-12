#!/usr/bin/env python3

import getopt, sys

#opts, args = getopt.getopt(sys.argv[1:], 'ho:',["help", "output="]) # "ho:"可以写成"-h-o:"

#print(opts)
#print(args)

opts, args = getopt.getopt(sys.argv[1:], '-h-f:-v', ['help', 'filename=', 'version'])
print(opts)
for opt_name, opt_value in opts:
	if opt_name in ('-h','--help'):
		print("[*] Help info")
		sys.exit()
	if opt_name in ('-v', '--version'):
		print("[*] Version is 0.01")
		sys.exit()
	if opt_name in ('-f','--filename'):
		filename = opt_value
		print("[*] Filename is ",filename)
		sys.exit()


