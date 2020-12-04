import threading
import queue
import urllib.parse
import urllib.request
import urllib.error


threads = 50
url_objetivo = "http://testphp.vulnweb.com"
dict = "C:\\all.txt"
user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:19.0) Gecko/20100101 Firefox/19.0"

def construir_dict(dict):
    print("Procesando diccionario...")

    arch = open(dict, "r") # Abrir archivo del diccionario
    raw_palabras = arch.readlines()
    arch.close()

    palabras = queue.Queue() # Se genera una instancia de la clase Queue (fila FIFO)

    for palabra in raw_palabras:
        palabra = palabra.rstrip()
        palabras.put(palabra)

    return palabras

def fuerza_bruta(fila_palabra, extensiones=None):
    while not fila_palabra.empty():
        intento = fila_palabra.get()

        lista_intento = []

        if '.' not in intento: # Revisa si es un directorio o una extension
            lista_intento.append("/%s/" % intento)
        else:
            lista_intento.append("/%s" % intento)

        if extensiones: # Si se quiere hacer fuerza bruta a extensiones
            for extension in extensiones:
                lista_intento.append("/%s%s" % (intento,extension))

        for i in lista_intento: # Comenzar la fuerza bruta
            url = "%s%s" % (url_objetivo,urllib.parse.quote(i))

            try:
                headers = {}
                headers["User-Agent"] = user_agent
                r = urllib.request.Request(url,headers=headers)

                respuesta = urllib.request.urlopen(r)

                if len(respuesta.read()):
                    print("[%d] => %s" % (respuesta.code,url))
            except urllib.error.URLError as e:
                if hasattr(e, 'code') and e.code != 404:
                    print("!!! %d => %s" % (e.code,url))
                pass

fila_palabras = construir_dict(dict)
extensiones = [".php",".bak",".orig",".inc"]

print("Comenzando fuerza bruta...")
for i in range(threads):
    t = threading.Thread(target=fuerza_bruta,args=(fila_palabras,extensiones,))
    t.start()