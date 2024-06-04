from twisted.internet import reactor, protocol
from twisted.protocols.basic import LineReceiver
import config

class ChatServer(LineReceiver):
    clients = []

    def connectionMade(self):
        self.clients.append(self)
        self.sendLine(b"Bienvenido al Chat del Servidor!")

    def connectionLost(self, reason):
        self.clients.remove(self)

    def lineReceived(self, line):
        message = f"<{self.transport.getHost()}> {line.decode('utf-8')}"
        for client in self.clients:
            if client != self:
                client.sendLine(message.encode('utf-8'))

class ChatServerFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return ChatServer()

if __name__ == "__main__":
    reactor.listenTCP(config.SERVER_PORT, ChatServerFactory())
    reactor.run()

