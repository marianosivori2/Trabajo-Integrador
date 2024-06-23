# Documentación Del Código

## `chat_server.py`
  
- Este archivo implementa el servidor de chat.

### 1. Importaciones necesarias:

```python
    from twisted.internet import reactor, protocol
    
    from twisted.protocols.basic import LineReceiver

    import config
```

`from twisted.internet import reactor, protocol`:

- reactor: Es el núcleo de Twisted que maneja el bucle de eventos y la E/S asíncrona. Es responsable de ejecutar el servidor y procesar eventos como conexiones entrantes y mensajes.

- protocol: Proporciona clases y funciones para crear y gestionar protocolos de red. En este caso, se usa para definir la fábrica del protocolo del servidor.


`from twisted.protocols.basic import LineReceiver`:

- LineReceiver: Es una clase base de Twisted que facilita el manejo de protocolos de línea, donde los mensajes están delimitados por líneas. Permite recibir y enviar mensajes línea por línea, lo cual es útil para la comunicación de texto.


`import config`:

- config: Importa un archivo de configuración que contiene la configuración del servidor y del cliente, como el puerto del servidor (SERVER_PORT). Esto permite que la configuración se centralice y se reutilice fácilmente en diferentes partes del proyecto.

### 2. Clase ChatServer: Maneja las conexiones de los clientes y la transmisión de mensajes.

```python
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
                self.sendLine(f"Bienvenido, {self.username}!".encode('utf-8'))
                self.sendLine(b"Escribe /salir para desconectarte del chat.")
                message = f"{self.username} se ha unido al chat."
                self.broadcast_message(message.encode('utf-8'))
            else:
                message = f"<{self.username}> {line.decode('utf-8')}"
                self.broadcast_message(message.encode('utf-8'))

        def broadcast_message(self, message):
            for client in self.clients:
                if client != self:
                    client.sendLine(message)
```

                
- clients = []: Lista que contiene todos los clientes conectados.
  
- connectionMade: Se llama cuando un cliente se conecta. Añade el cliente a la lista y envía un mensaje de bienvenida.

- connectionLost: Se llama cuando un cliente se desconecta. Elimina el cliente de la lista y envía un mensaje notificando que este usuario se desconectó

- lineReceived: Se llama cuando se recibe un mensaje. Envía el mensaje a todos los clientes conectados, excepto al que lo envió.

- broadcast_message: Método para enviar un mensaje a todos los clientes, exceptuando al emisor del mismo.

### 3. Clase ChatServerFactory: Crea instancias de ChatServer para manejar nuevas conexiones.

```python 
    class ChatServerFactory(protocol.Factory):
        def buildProtocol(self, addr):
            return ChatServer()
```

- buildProtocol: Método para crear y devolver una instancia de `ChatServer` cuando se establece una nueva conexión

### 4. Inicio del Servidor

```python
    if __name__ == "__main__":
        reactor.listenTCP(config.SERVER_PORT, ChatServerFactory())
        print(f"Servidor abierto en el puerto {config.SERVER_PORT}")
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

`from twisted.internet import reactor, protocol`:

- reactor: Igual que en el servidor, el reactor maneja el bucle de eventos y la E/S asíncrona para el cliente.

- protocol: Utilizado para definir la fábrica del protocolo del cliente, facilitando la creación y gestión de la conexión con el servidor.

  
`from twisted.protocols.basic import LineReceiver`: 

- LineReceiver: Igual que en el servidor, facilita el manejo de la comunicación de línea en el cliente, permitiendo recibir y enviar mensajes línea por línea.

`import config`:

- config: Igual que en el servidor, importa el archivo de configuración que contiene la configuración del servidor y del cliente, permitiendo utilizar configuraciones centralizadas, como el puerto del servidor.



### 2. Clase ChatClient: Maneja la conexión al servidor y la recepción de mensajes.

```python
    class ChatClient(LineReceiver):
        def connectionMade(self):
            self.prompt_for_username()

        def lineReceived(self, line):
            print(line.decode('utf-8'))
            if self.username:
                self.prompt_for_message()

        def prompt_for_username(self):
            self.username = input("Por favor, ingresa tu nombre de usuario: ")
            self.sendLine(self.username.encode('utf-8'))

        def prompt_for_message(self):
            reactor.callInThread(self.get_input)

        def get_input(self):
            while True:
                message = input()
                if message == '/salir':
                    reactor.callFromThread(self.transport.loseConnection)
                    break
                reactor.callFromThread(self.sendLine, message.encode('utf-8'))


```

- connectionMade: Se llama cuando se establece la conexión con el servidor. Envía un mensaje inicial al servidor.

- lineReceived: Se llama cuando se recibe un mensaje del servidor. Imprime el mensaje en la consola.

- prompt_for_username: Método que solicita al usuario que ingrese su nombre antes de ingresar al servidor.

- prompt_for_message: Este métopo maneja la solicitud de ingreso de mensajes.

- get_imput: Con esta función se puede recibir mensajes del servidor, y ademas, si detecta el comando especifico para desconectarse, devuelve un break que logra la desconexión.


### 3. Clase ChatClientFactory: Crea instancias de ChatClient y maneja la conexión.

```python
    class ChatClientFactory(protocol.ClientFactory):
        def buildProtocol(self, addr):
        return ChatClient()

        def clientConnectionFailed(self, connector, reason):
            print("Error de Conexión")
            reactor.stop()

        def clientConnectionLost(self, connector, reason):
            print("Te has desconectado")
            reactor.stop()

```

- buildProtocol: Crea y devuelve una instancia de ChatClient.
  
- clientConnectionFailed: Se llama cuando la conexión al servidor falla. Imprime un mensaje de error y detiene el reactor.

- clientConnectionLost: Se llama cuando el usuario se desconecta del servidor. Imprime un mensaje y detiene el reactor.


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
