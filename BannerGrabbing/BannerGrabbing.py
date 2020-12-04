import socket

def banner(ip, port):
    try:
        s = socket.socket()
        s.settimeout(4)
        s.connect((ip, int(port)))
        if port == 80 or port == 8080:
            s.send(b"HEAD / HTTP/1.1\r\n\r\n")
            print("Banner: " + s.recv(1024).decode())
        else:
            print("Banner: " + s.recv(1024).decode())
        s.close()
    except:
        pass


def scanports(ip,ports):
    for p in ports:
        try:
            s = socket.socket()
            r = s.connect_ex((ip,p))
            s.close()

            if r == 0:
                service = socket.getservbyport(p)

                print("[*] Open port: " + str(p) + " - Service: " + service)
                banner(ip,p)
            else:
                pass
        except:
            pass


ip = input("Ingresa la direccion IP a escanear: ")
ports = [20,21,22,25,80,110,113,443,3306,8443]
scanports(ip,ports)

