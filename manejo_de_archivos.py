# abrir archivo con metodo open()
"""
try:
    archivo = open("C:\\Users\\esteb\\Documents\\fire.txt")
except OSError as err:
    print("Error: " + str(err))
else:
    print(archivo.name)
    print(archivo.mode)
    print(archivo.closed)


# script para obtener el contenido de un archivo

# for linea in archivo:
 #   print(linea)


# print(archivo.read())
# print(archivo.red(5))
print(archivo.readline()) #con este metodo imprime el contenido del archivo


archivo.close()
"""

try:
    archivo2 = open("C:\\Users\\esteb\\Documents\\archivo2.txt", "w+")
    archivo2.write("Hola \n mundo")
    archivo2.seek(0) 
    print(archivo2.read())
except OSError as err:
    print("Error: " + str(err))
else:
    archivo2.close
