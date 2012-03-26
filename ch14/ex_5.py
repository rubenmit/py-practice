from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor

class SimpleLogger(Protocol):
    
    # when got a connection
    def connectionMade(self):
        print 'Got connection from', self.transport.client

    # call if lost a connection
    def connectionLost(self, reason):
        print self.transport.client, 'disconnected'

    def dataReceived(self, data):
        print data

factory = Factory()
factory.protocol = SimpleLogger

reactor.listenTCP(1234, factory)
reactor.run()
