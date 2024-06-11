from twisted.internet import reactor, protocol
from twisted.protocols.basic import LineReceiver
import config

class ChatClient(LineReceiver):
    def connectionMade(self):
        self.sendLine(b"Hola, Servidor!")

    def lineReceived(self, line):
        print(f"Server: {line.decode('utf-8')}")

    def sendMessage(self, message):
        self.sendLine(message.encode('utf-8'))

    def connectionLost(self, reason):
        print("Se perdió la Conexión")

class ChatClientFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return ChatClient()

    def clientConnectionFailed(self, connector, reason):
        print("Error de Conexión")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Se perdió la Conexión")
        reactor.stop()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python chat_client.py <host>")
        sys.exit(1)
    host = sys.argv[1]
    client_factory = protocol.ClientFactory()
    client_factory.protocol = ChatClient
    reactor.connectTCP(host, 8000, client_factory)
    reactor.run()
