import Pyro4

@Pyro4.expose
class GreetingMaker(object):
    def get_fortune(self, name):
        print('Someone called get_fortune method')
	return nameServer + ": Hello, {0}. Here is your fortune message:\n" \
               "Tomorrow's lucky number is 12345678.".format(name)

    aMessages = list()

    def messageStorage(self, message):
        self.aMessages.append(message)
        print aMessages

    def echoService(self, message):
        self.messageStorage(message)
        return nameServer + ": " + str(message)

    def showMessages(self):
        return self.aMessages

    def deleteMessageSeq(self, seq):
        if aMessages is None:
            return  "\nYou did not send any message yet.\n\n"
        elif aMessages.length < seq-1:
            return "\nMessage at ", seq-1, "position not found.\n"
        else:
            self.aMessages.pop(seq-1)
            return "\nMessage deleted successfully!\n"  

    def deleteMessageContent(self, message):
        if aMessages is None:
            return  "\nYou did not send any message yet.\n\n"
        cont = 0
        for messages in aMessages:
            if messages == message:
                self.aMessages.remove(message)
                cont = cont+1
        
        if cont == 0:
            return "Messages containing content: " + message + "not found.\n"
        else:
            return "\nMessage deleted successfully!\n"

nameServer = raw_input('Insert server name: ')

daemon = Pyro4.Daemon()                # make a Pyro daemon
ns = Pyro4.locateNS()                  # find the name server
uri = daemon.register(GreetingMaker)   # register the greeting maker as a Pyro object
ns.register('greeting-' + nameServer, uri)   # register the object with a name in the name server

print("Ready.")
daemon.requestLoop()                   # start the event loop of the server to wait for calls

