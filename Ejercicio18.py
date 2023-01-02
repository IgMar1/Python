#Funcion que recibe una URL y devuelve la cita en APPA

import requests
from bs4 import BeautifulSoup

def obtenerCitaAPA(url):
  # Primero, utilizamos la biblioteca requests para obtener el contenido de la página web
  respuesta = requests.get(url)
  
  # Luego, utilizamos la biblioteca BeautifulSoup para parsear el contenido de la página
  soup = BeautifulSoup(respuesta.text, 'html.parser')
  
  # Obtenemos el título de la página
  titulo = soup.title.string
  
  # Obtenemos el autor de la página
  autor = soup.find('meta', {'name': 'author'})
  
  # Si no se encuentra el metadato "author", se asigna un valor vacío a la variable "autor"
  if autor is None:
    autor = ""
  else:
    autor = autor['content']
  
  # Obtenemos la fecha de publicación de la página
  fecha = soup.find('meta', {'name': 'date'})
  
  # Si no se encuentra el metadato "date", se asigna un valor vacío a la variable "fecha"
  if fecha is None:
    fecha = ""
  else:
    fecha = fecha['content']
  
  # Creamos la cita en formato APA septima edición
  cita = f"{autor} ({fecha}). {titulo}."
  referencia = f"{autor}. ({fecha}). {titulo}. Recuperado de {url}"
  return cita, referencia


cita,referencia = obtenerCitaAPA("https://www.kali.org/tools/")
print(cita)
print(referencia)
