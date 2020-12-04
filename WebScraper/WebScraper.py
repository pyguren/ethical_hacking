from bs4 import BeautifulSoup
import requests

url = "http://www.howtowebscrape.com/examples/simplescrape1.html"
webpage = requests.get(url)

soup = BeautifulSoup(webpage.content, "html.parser")

print(soup.head) #Obtiene la etiqueta head de la pagina
print(soup.title) #Obtiene la etiqueta titulo de la pagina
print(soup.h1) # Obtiene la primera etiqueta h1
print(soup.div.i) # Obtiene la primera etiqueta i de la primera etiqueta div

centercon = soup.center.contents # Obtiene las etiquetas hijas de una etiqueta padre
print(centercon)
print(centercon[1]) #Obtiene la etiqueta hija en la posicion 1
print(centercon[3]) #Obtiene la etiqueta hija en la posicion 3

# Obtiene todas las cadenas que contengan las etiquetas
for s in soup.stripped_strings:
    print("String: " + s)

# Busqueda del primer elemento que contenga el id especificado
r = soup.find(id='ProductDetails')
print(r)

# Obtener el contenido de un elemento
print(r.text)

# Obtener todas las etiquetas div
r = soup.find_all('div')
for div_tag in r:
    print(div_tag)

# Obtiene el valor de un atributo de una etiqueta HTML
print("\nValor del atributo IMG:")
r = soup.find('img')
# forma 1
print(r['src'])
# forma 2
print(r.get('src'))