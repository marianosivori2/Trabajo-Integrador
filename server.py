from twisted.internet import reactor, protocol
from twisted.protocols.basic import LineReceiver
import config

class ChatServer(LineReceiver):
    clients = []

    def __init__(self):
        self.username = None

    def connectionLost(self, reason):
        if self.username:
            self.clients.remove(self)
            message = f"{self.username} se ha desconectado."
            self.broadcast_message(message.encode('utf-8'))

    def lineReceived(self, line):
        if self.username is None:
            self.username = line.decode('utf-8')
            self.clients.append(self)
            self.sendLine(f"Bienvenido, {self.username}! Si quieres desconectarte, TIPEA /salir".encode('utf-8'))
            message = f"{self.username} se ha unido al chat."
            self.broadcast_message(message.encode('utf-8'))
        else:
            message = f"<{self.username}> {line.decode('utf-8')}"
            self.broadcast_message(message.encode('utf-8'))

    def broadcast_message(self, message):
        for client in self.clients:
            if client != self:
                client.sendLine(message)

class ChatServerFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return ChatServer()

if __name__ == "__main__":
    reactor.listenTCP(config.SERVER_PORT, ChatServerFactory())
    print(f"Servidor abierto en el puerto {config.SERVER_PORT}")
    reactor.run()
