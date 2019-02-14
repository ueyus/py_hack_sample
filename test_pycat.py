import sys
import socket
import getopt
import threading
import subprocess

listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0

def usage():
	print　"bhp net tool"
	print
	print "Usage bhpnet.py -t target_host -p port"
	print "-l --listen"
	print
	sys.exit(0)

def main():
	global listen
	global port
	global execute
	global command
	global upload_destination
	global target

	if not len(sys.argv[1:]):
		usage()

	try:
		opts, args = getopt.getopt(
			sys.argv[1:],
			"hle:t:p:cu:"
			["help", "listen", "execute=", "target=",
			"port=", "command", "upload="])
	except getopt.GetoptError as err:
		print str(err)
		usage()

	for o, a in opts:
		if o in ("-h", "--help"):
			usage()
		else:
			assert False, "Unhandled Option"

	if not listen and len(target) and port > 0:
		buffer = sys.stdin.read()
		clien_sender(buffer)

	if listen:
		server_loop()

main()