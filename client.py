import Pyro4
import os
import sys

HOST='localhost'
PORT=9090

if len(sys.argv) == 2 or len(sys.argv) > 3:
	print('''
If you want to connect to a specific server you need to inform host and port.
Ex: python client.py localhost 9090
Or just run "$ python client.py" to use the default settings.
''')
	exit()

if len(sys.argv) == 3:
	HOST = sys.argv[1]
	try:
		PORT = int(sys.argv[2])
	except ValueError:
		print('%s is a invalid value for port.' % sys.argv[2])
		exit()

def tryToUseMethodAnyServer(method, *args):

	try:
		ns = Pyro4.locateNS(host=HOST,port=PORT)
		server_names = ns.list('rmiserver-') #this should be returning me all servers registered on pyro's nameserver
		keys = list(server_names.keys())
	except Pyro4.errors.NamingError:
		print("\nFailed to locate the nameserver on %s:%d. Make sure it's running, execute: \n\npyro4-ns -n %s -p %d\n" % (HOST,PORT,HOST,PORT) )
		return False

	for key in keys:
		each_server = Pyro4.Proxy(server_names[key])

		try:
			return getattr(each_server, method)(*args)
		except Pyro4.errors.CommunicationError:
			pass
	
	print("Can't find any server available.")
	return False

while True:
	os.system('clear')
	print "#-----------------------------------------#"
	print "#               MENU APP                  #"
	print "# Options:                                #"
	print "# [1] Echo Service                        #"
	print "# [2] Echoed Messages List                #"
	print "# [0] Exit                                #"
	print "#-----------------------------------------#"
	try:
		option = raw_input("Choose an option: ")
	except KeyboardInterrupt:
		print('\nThe connection was finished successfully...')
		break

	if option == "1":
		try:
			message = raw_input("Write your message: ")
		except KeyboardInterrupt:
			print('\nThe connection was finished successfully...')
			break
		returnedMessage = tryToUseMethodAnyServer('echoService', message)
		if returnedMessage:
			print(returnedMessage)
	elif option == "2":
		returnedMessage = tryToUseMethodAnyServer('getMessages')
		if returnedMessage:
			for message in returnedMessage[1]:
				print ("-" + message)
			print('Messages returned from server ' + returnedMessage[0])
	elif option == "0":
		print('The connection was finished successfully...')
		break
	else:
		print('Option not available.')
	
	raw_input('Press Enter to continue...')