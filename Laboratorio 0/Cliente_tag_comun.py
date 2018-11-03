import socket

servidor = "127.0.0.1"
puerto = 5555

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cliente.sendto("Este mensaje ha sido enviado por el cliente", (servidor,puerto));