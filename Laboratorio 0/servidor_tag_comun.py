import socket
import threading
 
ip = "0.0.0.0" 
puerto = 5555 
max_conexiones = 5 

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

servidor.bind((ip, puerto))

print ("[*] Esperando conexiones en %s:%d" % (ip, puerto))

while True:
    dato, direccion = servidor.recvfrom(1024)
    print ("[*] La conexion se ha establecido con %s:%d" % (direccion[0] , direccion[1]))
    print ("[*] El mensaje ha sido recibido: %s" % dato)