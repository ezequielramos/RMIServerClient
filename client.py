import Pyro4
import sys

try:
	ns = Pyro4.locateNS()
	server_names = ns.list('rmiserver-') #this should be returning me all servers registered on pyro's nameserver
except Pyro4.errors.NamingError:
	print("\nFailed to locate the nameserver. Make sure it's running, execute: \n\npyro4-ns\n")
	exit()

keys = list(server_names.keys())

if len(keys) == 0:
	print("\nCan't find any server available.\n")
	exit()

greeting_maker = Pyro4.Proxy(server_names[keys[0]]) #try to connect to the first server 

aMessages = list()

def messages(greeting_maker):
    if greeting_maker:
        aMessages = greeting_maker.showMessages()
        if aMessages:
            print ("Echoed Messages below: \n")
            for message in aMessages:
                print (" - " + str(message) + "\n")
        else:
            print ("\nYou did not send any message yet.\n\n")

while True:
	try:
		print "#-----------------------------------------#"
		print "#               MENU APP                  #"
		print "# Options:                                #"
		print "# [1] Echo Service                        #"
		print "# [2] Echoed Messages List                #"
		print "# [3] Delete Message by seq number        #"
		print "# [4] Delete Message by content           #"
		print "# [5] Exit                                #"
		print "#-----------------------------------------#"
		option = int(input("Choose one option: "))

		if option == 1:
			message = raw_input("Write your message: ")
			print (greeting_maker.echoService(message))
		elif option == 2:
			try:
				messages(greeting_maker)
			except:
				print ("\nSomething is wrong.\n\n")
		elif option == 3:
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
				print ("\nSomething is wrong.\n\n")
		elif option == 5:
				print ("\n\nThe connection was finished successfully...\n")
				break

	except Pyro4.errors.CommunicationError: #if failed to connect to the first server try with the second one
		greeting_maker = Pyro4.Proxy(server_names[keys[1]])
		#print(greeting_maker.get_fortune(name))