import getopt
import sys


opts,args = getopt.getopt(sys.argv[1:], '-h-f:-v', ['help', 'filename=','version']

for opt_name, opt_value in opts:
	if opt_name in ('-h', '--help'):
		print("[*] Help info")
		sys.exit()
	if opt_name in ('-v', '--version'):
		print("[*] Vesion is 0.001")
		sys.exit()
	if opt_name in ('-f', '--filename'):
		fileNmae = opt_value
		print("[*] Filename is ", fileName)
		sys.exit()
