from twisted.internet import reactor, protocol
from twisted.internet.protocol import Protocol
from twisted.internet.protocol import ServerFactory as serverFactory
from twisted.internet.endpoints import TCP4ServerEndpoint

import os
import time

def initialize():
    print("Initializing...")

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
    endpoint = TCP4ServerEndpoint(reactor, 2000)
    endpoint.listen(ServerFactory())
    reactor.run()
