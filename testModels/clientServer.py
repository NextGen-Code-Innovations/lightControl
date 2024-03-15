from twisted.internet import reactor, protocol
from twisted.internet.protocol import Protocol
# server things
from twisted.internet.protocol import ServerFactory as serverFactory
from twisted.internet.endpoints import TCP4ServerEndpoint as serverEndpoint
# client things
from twisted.internet.protocol import ClientFactory as clientFactory
from twisted.internet.endpoints import TCP4ClientEndpoint as serverEndpoint

#==========================================================================
#============================ Server things ===============================
#==========================================================================
class Server(Protocol):
    def connectionMade(self):
        print("new connection")
        self.transport.write("Hello from server".encode("utf-8"))
        
    def dataRecieved(self, data):
        print(data)
        self.transport.write(data)

class ServerFactory(serverFactory):
    def buildProtocol(self, addr):
        return Server()

if __name__ == '__main__':
    endpoint = serverEndpoint(reactor, 2000)
    endpoint.listen(ServerFactory())
    reactor.run()

#==========================================================================
#=========================== Client things ================================
#==========================================================================
class Client(Protocol):
    def dataRecieved(self, data):
        data = data.decode("utf-8")
        print(data)
        self.transport.write(input(":::").encode("utf-8"))

class ClientFactory(clientFactory):
    def buildProtocol(self, addr):
        return  Client()
    
if __name__ == '__main__':
        endpoint = clientFactory(reactor, 'localhost', 2000)
        endpoint.connect(ClientFactory())
        reactor.run()

