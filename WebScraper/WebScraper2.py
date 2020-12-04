from bs4 import BeautifulSoup
import requests

url = "https://www.porrua.mx/busqueda/todos/hacking"
webpage = requests.get(url)

soup = BeautifulSoup(webpage.content, "html.parser")

all_libros = soup.find('div', id='librosContainer')

libros = all_libros.find_all('div')
for lib in libros:
    a = lib.find('a')
    if a != None:
        link = a['href']
        titulo = a.find('h5').text.split("\n")[0]
        autor = a.find('i').text
        precio = a.find('strong').text
        print("\nTitulo: " + titulo)
        print("Autor: " + autor)
        print("Precio: " + precio)
        print("Link: " + link)