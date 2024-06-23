# Servidor de Chat con Twisted

Este proyecto crea un servidor de chat utilizando el framework Twisted. Permite que varios usuarios se conecten y chateen en tiempo real.

## Archivos

- `server.py`: Contiene la implementación del servidor de chat.
- `cliente.py`: Contiene la implementación del cliente de chat.
- `config.py`: Contiene la configuración del servidor y del cliente.
- `README.md`: Este archivo contiene las instrucciones sobre cómo usar el programa.
- `DOCU.md`: Este archivo contiene la documentación y explicación del código

## Requisitos
- Repositorio
- Python 3.x
- Twisted

## Instalación

1. Descargá el repositorio

2. Instalá Twisted usando pip:

Abriremos la consola (cmd) y tipearemos "pip install twisted"

```cmd
pip install twisted
```

## Uso
### 1. Ubicá el repositorio

Abriremos una ventana cmd, y escribiremos "cd" y a su lado la ruta del repositorio.

```cmd
cd *ruta de repositorio*
```

### 2. Iniciá el servidor de chat:

Una vez ubicada la ruta en el cmd, ejecutaremos este codigo que se encargará de alojar el servidor.

```cmd
python server.py
```

- Solamente el que hostea el servidor se encarga de ejecutar este comando

### 3. Conectate al servidor de chat desde un cliente:

Luego, abriremos otra ventana cmd para ejecutar este codigo, el cual se une al servidor alojado.

```cmd
python cliente.py <host>
```

- Reemplazá `<host>` con la dirección IP donde se está ejecutando el servidor.

### 4. Escribí mensajes en el cliente para enviarlos al servidor, y estos serán retransmitidos a todos los clientes conectados.

## Configuración

- Podés cambiar el puerto del servidor editando el archivo `config.py`:

```python
SERVER_PORT = 8000
```

