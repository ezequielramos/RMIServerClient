import Pyro4
from rmiechoserver import RMIEchoServer

daemon = Pyro4.Daemon() # make a Pyro daemon
try:
    ns = Pyro4.locateNS() # find the name server
except Pyro4.errors.NamingError:
    print("\nFailed to locate the nameserver. Make sure it's running, execute: \n\npyro4-ns\n")
    exit()

name_server = ''

while name_server.strip() == '':
    name_server = raw_input('Insert server name: ')

rmiEchoServer = RMIEchoServer(name_server)

uri = daemon.register(rmiEchoServer) # register the greeting maker as a Pyro object
ns.register('rmiserver-' + name_server, uri) # register the object with a name in the name server

print("Ready.")
daemon.requestLoop() # start the event loop of the server to wait for calls