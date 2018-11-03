import socket
import sys
import select

arglen=len(sys.argv)
if arglen<3:
    print('Ejemplo: python2 cliente_chat.py 0.0.0.0 5000')
    exit()

addr=sys.argv[1]
port=int(sys.argv[2])

timeout_in_seconds=60
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print >>sys.stderr, 'conectando a %s puerto %d' % (addr, port)

nombre = raw_input("Ingresa tu nombre ")

cliente.connect((addr,port))
cliente.sendall(nombre)


while True:
    mensaje = raw_input(nombre + "> ")
    cliente.sendall(mensaje)
    ready = select.select([cliente], [], [], timeout_in_seconds)
    if ready[0]:
        respuesta = cliente.recv(1024)
        if respuesta == "exit":
            cliente.close()
            print("Sesion finalizada")
        else:
            print ('Servidor> '+ respuesta)
    else:
        cliente.close()
        print("Sesion Finalizada")
        break
