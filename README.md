# Servidor de Chat con Twisted

Este proyecto implementa un servidor de chat simple usando el framework Twisted. Permite a múltiples clientes conectarse y chatear en tiempo real.

## Archivos

- `chat_server.py`: Contiene la implementación del servidor de chat.
- `chat_client.py`: Contiene la implementación del cliente de chat.
- `protocols.py`: Define el protocolo de comunicación entre el servidor y los clientes.
- `config.py`: Contiene la configuración del servidor y del cliente.
- `README.md`: Este archivo, con instrucciones sobre cómo usar el proyecto.

## Requisitos

- Python 3.x
- Twisted

## Instalación

Instala Twisted usando pip:

pip install twisted

## Uso

1. Inicia el servidor de chat:

python chat_server.py

2. Conéctate al servidor de chat desde un cliente:

python chat_client.py <host>


Reemplaza `<host>` con la dirección IP o el nombre del host donde se está ejecutando el servidor.

3. Escribe mensajes en el cliente para enviarlos al servidor, y estos serán retransmitidos a todos los clientes conectados.

## Configuración

Puedes cambiar el puerto del servidor editando el archivo `config.py`:

```python
SERVER_PORT = 8000

Licencia
Este proyecto está licenciado bajo la Licencia MIT.

Con esta estructura, tienes un archivo adicional `config.py` que maneja la configuración del servidor y del cliente, haciendo el proyecto más modular y fácil de mantener.
