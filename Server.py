import socket
import threading

clientes = []
nombres = []

def broadcast(mensaje):
    for cliente in clientes:
        cliente.send(mensaje)

def manejar_cliente(cliente):
    while True:
        try:
            mensaje = cliente.recv(1024)
            broadcast(mensaje)
        except:
            index = clientes.index(cliente)
            clientes.remove(cliente)
            cliente.close()
            nombre = nombres[index]
            broadcast(f"{nombre} se desconectó".encode('utf-8'))
            nombres.remove(nombre)
            break

def recibir():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(('0.0.0.0', 12345))
    servidor.listen()

    print("Servidor corriendo...")

    while True:
        cliente, direccion = servidor.accept()
        print(f"Conectado con {str(direccion)}")

        cliente.send("NOMBRE".encode('utf-8'))
        nombre = cliente.recv(1024).decode('utf-8')

        nombres.append(nombre)
        clientes.append(cliente)

        print(f"Nombre del cliente: {nombre}")
        broadcast(f"{nombre} se unió al chat".encode('utf-8'))

        thread = threading.Thread(target=manejar_cliente, args=(cliente,))
        thread.start()

recibir()
