import Pyro4

@Pyro4.expose
class RMIEchoServer(object):

    def __init__(self, name_server):
        self.aMessages = list()
        self.name_server = name_server

    def sendMessageToReplicas(self, name_server, message):
        ns = Pyro4.locateNS()
        server_names = ns.list('rmiserver-') #this should be returning me all servers registered on pyro's nameserver
        keys = list(server_names.keys())

        for key in keys:
            each_server = Pyro4.Proxy(server_names[key])
            try:
                each_server.receiveMessageToReplica(name_server, message)
            except Pyro4.errors.CommunicationError:
                print('Can\'t send message to server ' + key.split('rmiserver-')[1])

    def receiveMessageToReplica(self, name_server, message):
        print('Received message from server ' + name_server)
        self.aMessages.append(message)

    def echoService(self, message):
        self.sendMessageToReplicas(self.name_server, str(message))
        print('Someone called my echoService :)')
        return self.name_server + ": " + str(message)

    def getMessages(self):
        print('Someone called my getMessages :)')
        return (self.name_server, self.aMessages)