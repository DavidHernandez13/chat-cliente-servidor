import socket
import threading

def recibir_mensajes(sock):
    while True:
        try:
            mensaje = sock.recv(1024)
            if mensaje:
                print(f"\n{mensaje.decode()}")
                print(">>", end="", flush=True)
        except:
            break

def cliente():
    host = input("IP del servidor: ")
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print("Conectado al chat grupal - Escribe 'exit' para salir")

    # Hilo para recibir mensajes
    thread = threading.Thread(target=recibir_mensajes, args=(client_socket,))
    thread.daemon = True
    thread.start()

    while True:
        mensaje = input(">>")
        if mensaje.lower() == 'exit':
            break
        try:
            client_socket.sendall(mensaje.encode())
        except:
            print("Error: conexión perdida")
            break

    client_socket.close()

if __name__ == "__main__":
    cliente()