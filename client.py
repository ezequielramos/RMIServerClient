import Pyro4
import os

def tryToUseMethodAnyServer(method, *args):

	try:
		ns = Pyro4.locateNS()
		server_names = ns.list('rmiserver-') #this should be returning me all servers registered on pyro's nameserver
		keys = list(server_names.keys())
	except Pyro4.errors.NamingError:
		print("\nFailed to locate the nameserver. Make sure it's running, execute: \n\npyro4-ns\n")
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
	'''print "# [3] Delete Message by seq number        #"
	print "# [4] Delete Message by content           #"'''
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