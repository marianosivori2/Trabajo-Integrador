from twisted.internet import reactor, protocol
from twisted.protocols.basic import LineReceiver
import config

class ChatClient(LineReceiver):
    def connectionMade(self):
        self.sendLine(b"Hola, Servidor!")
        self.transport.write(b"Escribe tu mensaje: ")

    def lineReceived(self, line):
        print(f"Server: {line.decode('utf-8')}")
        self.transport.write(b"Escribe tu mensaje: ")

    def rawDataReceived(self, data):
        pass

    def lineLengthExceeded(self, line):
        print("ERROR: Mensaje demasiado largo.")

    def connectionLost(self, reason):
        pass

    def write(self, line):
        self.sendLine(line.encode('utf-8'))


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
    import sys
    if len(sys.argv) != 2:
        print("Usage: python chat_client.py <host>")
        sys.exit(1)
    host = sys.argv[1]
    reactor.connectTCP(host, config.SERVER_PORT, ChatClientFactory())
    reactor.run()
