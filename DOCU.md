# Documentación Del Código

## `chat_server.py`
  
- Este archivo implementa el servidor de chat.

### 1. Importaciones necesarias:

```python
    from twisted.internet import reactor, protocol
    
    from twisted.protocols.basic import LineReceiver

    import config
```

### 2. Clase ChatServer: Maneja las conexiones de los clientes y la transmisión de mensajes.

```python
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
```

                
- clients = []: Lista que contiene todos los clientes conectados.
  
- connectionMade: Se llama cuando un cliente se conecta. Añade el cliente a la lista y envía un mensaje de bienvenida.

- connectionLost: Se llama cuando un cliente se desconecta. Elimina el cliente de la lista.

- lineReceived: Se llama cuando se recibe un mensaje. Envía el mensaje a todos los clientes conectados, excepto al que lo envió.

### 3. Clase ChatServerFactory: Crea instancias de ChatServer para manejar nuevas conexiones.

```python 
    class ChatServerFactory(protocol.Factory):
        def buildProtocol(self, addr):
            return ChatServer()
```

### 4. Inicio del Servidor

```python
    if __name__ == "__main__":
      reactor.listenTCP(config.SERVER_PORT, ChatServerFactory())
      reactor.run()
```
- "reactor.listenTCP(config.SERVER_PORT, ChatServerFactory())": Configura el servidor para aceptar conexiones en el puerto especificado.

- "reactor.run()": Inicia el bucle de eventos del servidor.
  

##  `chat_client.py`
  
- Este archivo implementa el cliente de chat.

### 1. Importaciones necesarias:

```python
    from twisted.internet import reactor, protocol
    from twisted.protocols.basic import LineReceiver
    import config

```

### 2. Clase ChatClient: Maneja la conexión al servidor y la recepción de mensajes.

```python
    class ChatClient(LineReceiver):

        def connectionMade(self):
            self.sendLine(b"Hola, Servidor!")

        def lineReceived(self, line):
            print(f"Server: {line.decode('utf-8')}")


```

- connectionMade: Se llama cuando se establece la conexión con el servidor. Envía un mensaje inicial al servidor.

- lineReceived: Se llama cuando se recibe un mensaje del servidor. Imprime el mensaje en la consola.


### 3. Clase ChatClientFactory: Crea instancias de ChatClient y maneja la conexión.

```python
    class ChatClientFactory(protocol.ClientFactory):

        def buildProtocol(self, addr):
            return ChatClient()

        def clientConnectionFailed(self, connector, reason):
            print("Error de Conexión")
            reactor.stop()

        def clientConnectionLost(self, connector, reason):
            print("Se perdió la Conexión")
            reactor.stop()
```

- buildProtocol: Crea y devuelve una instancia de ChatClient.
  
- clientConnectionFailed: Se llama cuando la conexión al servidor falla. Imprime un mensaje de error y detiene el reactor.

- clientConnectionLost: Se llama cuando la conexión al servidor se pierde. Imprime un mensaje y detiene el reactor.


### 4. Inicio del cliente:

```python
    if __name__ == "__main__":
        import sys
        if len(sys.argv) != 2:
            print("Usage: python chat_client.py <host>")
            sys.exit(1)
    host = sys.argv[1]
    reactor.connectTCP(host, config.SERVER_PORT, ChatClientFactory())
    reactor.run()
```

- Verifica que se ha proporcionado un host como argumento.

- reactor.connectTCP(host, config.SERVER_PORT, ChatClientFactory()): Conecta al servidor en el host y puerto especificados.

- reactor.run(): Inicia el bucle de eventos del cliente.


## `config.py`

- Este archivo contiene la configuración del servidor y del cliente.

```python
SERVER_PORT = 8000
```
