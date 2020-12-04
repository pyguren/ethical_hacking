import hashlib

hash_a_romper = "5f4dcc3b5aa765d61d8327deb882cf99"

ruta = "C:\\Users\\esteb\\Documents\\fire.txt"

try:
    diccionario = open(ruta, "r")
except OSError as err:
    print("Error: " + str(err))
else:
    print("\nComenzando el crackeo...")
    for contrasenia in diccionario:
        print("[*] Probando: " + contrasenia)
        hash_c = hashlib.md5(contrasenia.encode('utf-8').strip()).hexdigest()
        if hash_c == hash_a_romper:
            print("\nContraseña encontrada:" + contrasenia)
            break
    diccionario.close()
