import socket
import sys

arglen=len(sys.argv)
if arglen<3:
    print('Ejemplo: python2 cliente_tag.py 0.0.0.0 5000')
    exit()

servidor=sys.argv[1]
puerto=int(sys.argv[2])

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

cliente.sendto("Este mensaje ha sido enviado por el cliente", (servidor,puerto));