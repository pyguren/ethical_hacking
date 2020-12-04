"""
print("\EJEMPLO DE FOR")
lista = ["azul", "amarillo", "rojo", "verde"]

for i in lista:
    print("Color: " + i)

print("\n EJEMPLO DE BREAK")
for s in "cadena"
   if s == "e":
        break
    else:
        print(s)

print("n\EJEMPLO DE CONTINUE")
for s in "abcdefghij":
    if s == "d":
        continue
    else:
        print(s)
"""

print("\n ESCAPES")
print("Ella dijo: \"Vamos a comer\"")


print("\n METODOS DE UN STRING")

s = "Hola mundo!"
print(s.lower())
print(s)
print(s.upper())
s1 = "esto es un ejemplo"
print(s1.capitalize())
print(s1.count("e"))
print(s1.split(" "))
print(s1.replace("ejemplo", "carrito"))

s2 = "    Hola mundo!    "
print("Ejemplo:" + s2 + ".")
print("Ejemplo:" + s2.strip() + ".")

print("\n EJEMPLO DE LISTAS")

abc = ["a", "b", "c", "d", "e"]
print(abc[0:3])
print(abc[:3])
print(abc[-3:])
print(abc[:])

print(abc)
abc.append("f")
print(abc)

abc.remove("c")
print(abc)

abc.sort()
print(abc)

abc.insert(2, "s")
print(abc)

abc.pop(2)
print(abc)


print("\n EJEMPLO DE FUNCIONES")


def imprime_lista(lista):
    print("elementos de la lista:")
    for i in lista:
        print(i)


lista1 = [1, 2, 3, 4, 5]
imprime_lista(lista1)


print("\n DICCIONARIOS")

agenda = {"alicia": "2345", "Beto": "7899", "cecilia": "1234"}
print["Beto"] = "0000"
pint(agenda)

for llave in agenda:
    Print(llave)

for llave in agenda:
    print(agenda[llave])

agenda["Pedro"] = "9876"
print(agenda)

agenda.pop("Cecilia")
print(agenda)
