import Pyro4

@Pyro4.expose
class RMIEchoServer(object):

    def __init__(self, name_server):
        self.aMessages = list()
        self.name_server = name_server

    def messageStorage(self, message):
        self.aMessages.append(message)
        print(self.aMessages)

    def echoService(self, message):
        self.messageStorage(message)
        return self.name_server + ": " + str(message)

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
