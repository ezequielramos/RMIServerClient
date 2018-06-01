import Pyro4
from rmiechoserver import RMIEchoServer

name_server = ''

while name_server.strip() == '':
    name_server = raw_input('Insert server name: ')

rmiEchoServer = RMIEchoServer(name_server)

daemon = Pyro4.Daemon() # make a Pyro daemon
try:
    ns = Pyro4.locateNS() # find the name server
    server_names = ns.list('rmiserver-') #this should be returning me all servers registered on pyro's nameserver
    keys = list(server_names.keys())

    for key in keys:
        each_server = Pyro4.Proxy(server_names[key])

        if key.split('rmiserver-')[1] == name_server:
            continue

        try:
            responseMessage = each_server.getMessages()
            rmiEchoServer.aMessages = responseMessage[1]
            print('Server %s send me %d messages.' % (responseMessage[0], len(responseMessage[1]) ) ) 
            break
        except Pyro4.errors.CommunicationError:
            print('Can\'t get messages from server ' + key.split('rmiserver-')[1])

    uri = daemon.register(rmiEchoServer) # register the greeting maker as a Pyro object
    ns.register('rmiserver-' + name_server, uri) # register the object with a name in the name server

    print("Ready.")
    daemon.requestLoop() # start the event loop of the server to wait for calls

except Pyro4.errors.NamingError:
    print("\nFailed to locate the nameserver. Make sure it's running, execute: \n\npyro4-ns\n")
    exit()