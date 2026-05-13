import socket
import threading

nombre = input("Ingresa tu nombre: ")

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('127.0.0.1', 12345))

def recibir():
    while True:
        try:
            mensaje = cliente.recv(1024).decode('utf-8')
            if mensaje == 'NOMBRE':
                cliente.send(nombre.encode('utf-8'))
            else:
                print(mensaje)
        except:
            print("Error de conexión")
            cliente.close()
            break

def escribir():
    while True:
        mensaje = f"{nombre}: {input('')}"
        cliente.send(mensaje.encode('utf-8'))

threading.Thread(target=recibir).start()
threading.Thread(target=escribir).start()
