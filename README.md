# Servidor de Chat con Twisted

Este proyecto crea un servidor de chat utilizando el framework Twisted. Permite que varios usuarios se conecten y chateen en tiempo real.

## Archivos

- `chat_server.py`: Contiene la implementación del servidor de chat.
- `chat_client.py`: Contiene la implementación del cliente de chat.
- `config.py`: Contiene la configuración del servidor y del cliente.
- `README.md`: Este archivo contiene las instrucciones sobre cómo usar el proyecto.
- `DOCU.md`: Este archivo contiene la documentación y explicación del código

## Requisitos

- Python 3.x
- Twisted

## Instalación

Instalá Twisted usando pip:

Abriremos la consola (cmd) y tipearemos "pip install twisted"

```cmd
pip install twisted
```

## Uso

### 1. Iniciá el servidor de chat:

En una ventana cmd, ejecutaremos este codigo que se encargará de alojar el servidor.

```cmd
python chat_server.py
```

- Solamente el que hostea el servidor se encarga de ejecutar este comando

### 2. Conectate al servidor de chat desde un cliente:

Luego, abriremos otra ventana cmd para ejecutar este codigo, el cual es el que se une al servidor alojado.

```cmd
python chat_client.py <host>
```

- Reemplazá `<host>` con la dirección IP donde se está ejecutando el servidor.

### 3. Escribí mensajes en el cliente para enviarlos al servidor, y estos serán retransmitidos a todos los clientes conectados.

## Configuración

- Podés cambiar el puerto del servidor editando el archivo `config.py`:

```python
SERVER_PORT = 8000
```

