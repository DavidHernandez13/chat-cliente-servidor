import socket
import threading

clientes = []

def manejar_cliente(conn, addr):
    print(f"Cliente conectado: {addr}")
    while True:
        try:
            mensaje = conn.recv(1024)
            if not mensaje:
                break
            mensaje_decodificado = mensaje.decode()
            print(f"{addr}: {mensaje_decodificado}")
            # Enviar mensaje a todos los clientes
            for cliente in clientes:
                try:
                    cliente.send(f"{addr}: {mensaje_decodificado}".encode())
                except:
                    pass
        except:
            break
    
    print(f"Cliente desconectado: {addr}")
    clientes.remove(conn)
    conn.close()

def servidor():
    host = '0.0.0.0'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Servidor de chat escuchando en {host}:{port}")

    while True:
        conn, addr = server_socket.accept()
        clientes.append(conn)
        thread = threading.Thread(target=manejar_cliente, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    servidor()