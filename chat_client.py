from twisted.internet import reactor, protocol
from twisted.protocols.basic import LineReceiver
import config

class ChatClient(LineReceiver):
    def connectionMade(self):
        self.sendLine(b"Hola, Servidor!")

    def connectionLost(self, reason):
        print("Se perdió la conexión con el servidor.")

    def lineReceived(self, line):
        print(f"Server: {line.decode('utf-8')}")

        # Permitir enviar mensajes continuamente después de recibir el mensaje de bienvenida
        self.prompt_for_messages()

    def prompt_for_messages(self):
        while True:
            message = input("Escribe tu mensaje (o escribe 'quit' para salir): ")
            if message.lower() == 'quit':
                self.transport.loseConnection()  # Cierra la conexión
                break
            else:
                self.sendLine(message.encode('utf-8'))

class ChatClientFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return ChatClient()

    def clientConnectionFailed(self, connector, reason):
        print("Error de conexión.")
        reactor.stop()

if __name__ == "__main__":
    reactor.connectTCP(config.SERVER_HOST, config.SERVER_PORT, ChatClientFactory())
    reactor.run()
