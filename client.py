import Pyro4

def tryToUseMethodAnyServer(method, *args):

	ns = Pyro4.locateNS()
	server_names = ns.list('rmiserver-') #this should be returning me all servers registered on pyro's nameserver
	keys = list(server_names.keys())

	for key in keys:
		each_server = Pyro4.Proxy(server_names[key])

		try:
			return getattr(each_server, method)(*args)
		except Pyro4.errors.CommunicationError:
			pass
	
	print("Can't find any server available.")
	return False

while True:
	print "#-----------------------------------------#"
	print "#               MENU APP                  #"
	print "# Options:                                #"
	print "# [1] Echo Service                        #"
	print "# [2] Echoed Messages List                #"
	print "# [3] Delete Message by seq number        #"
	print "# [4] Delete Message by content           #"
	print "# [0] Exit                                #"
	print "#-----------------------------------------#"
	option = int(input("Choose one option: "))

	if option == 1:
		message = raw_input("Write your message: ")
		returnedMessage = tryToUseMethodAnyServer('echoService', message)
		if returnedMessage:
			print(returnedMessage)
	elif option == 2:
		returnedMessage = tryToUseMethodAnyServer('getMessages')
		if returnedMessage:
			for message in returnedMessage[1]:
				print ("-" + message)
			print('Messages returned from server ' + returnedMessage[0])
	elif option == 0:
		print ('The connection was finished successfully...')
		break
	'''elif option == 3:
		try:
			messageSeq = input("Inform the seq number: ")
			print (greeting_maker.deleteMessageSeq(messageSeq))
		except:
			print ("\nSomething is wrong.\n\n")
	elif option == 4:
		try:
			message = raw_input("Inform the message: ")
			print (greeting_maker.deleteMessageContent(message))
		except:
			print ("\nSomething is wrong.\n\n")'''
