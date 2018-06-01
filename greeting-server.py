import Pyro4


@Pyro4.expose
class GreetingMaker(object):

    def __init__(self):
        self.aMessages = list()

    def messageStorage(self, message):
        self.aMessages.append(message)
        print(self.aMessages)

    def echoService(self, message):
        self.messageStorage(message)
        return nameServer + ": " + str(message)

    def showMessages(self):
        return self.aMessages

    def deleteMessageSeq(self, seq):
        if self.aMessages is None:
            return  "\nYou did not send any message yet.\n\n"
        elif len(self.aMessages) < seq-1:
            return "\nMessage at ", seq-1, "position not found.\n"
        else:
            self.aMessages.pop(seq-1)
            return "\nMessage deleted successfully!\n"  

    def deleteMessageContent(self, message):
        if self.aMessages is None:
            return  "\nYou did not send any message yet.\n\n"
        cont = 0
        for messages in self.aMessages:
            if messages == message:
                self.aMessages.remove(message)
                cont = cont+1
        
        if cont == 0:
            return "Messages containing content: " + message + "not found.\n"
        else:
            return "\nMessage deleted successfully!\n"

daemon = Pyro4.Daemon()                # make a Pyro daemon
try:
    ns = Pyro4.locateNS()                  # find the name server
except Pyro4.errors.NamingError:
    print("\nFailed to locate the nameserver. Make sure it's running, execute: \n\npyro4-ns\n")
    exit()

nameServer = raw_input('Insert server name: ')

uri = daemon.register(GreetingMaker)   # register the greeting maker as a Pyro object
ns.register('greeting-' + nameServer, uri)   # register the object with a name in the name server

print("Ready.")
daemon.requestLoop()                   # start the event loop of the server to wait for calls