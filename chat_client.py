from twisted.internet import reactor, protocol
from twisted.protocols.basic import LineReceiver
import config

class ChatClient(LineReceiver):
    def connectionMade(self):
        self.sendLine(b"Hola, Servidor!")
    
    def lineReceived(self, line):
        print(f"Server: {line.decode('utf-8')}")
    
        if line.strip() == b"Bienvenido al Chat del Servidor!":
            self.prompt_for_message()

    def prompt_for_message(self):
        message = input("Escribe tu mensaje ('quit' para salir): ")
        if message.lower() == "quit":
            self.transport.loseConnection() 
        else:
            self.sendLine(message.encode('utf-8'))
            self.prompt_for_message()

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
