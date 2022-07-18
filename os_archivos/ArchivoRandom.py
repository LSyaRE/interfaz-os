import random
import string
from tkinter import Variable

class ArchivoRandom:
  def __init__(self) -> None:
    self.nombre='str'

  #Generar caracteres aleatorios y cantidad de palabras 
  def random_caracter(self):
    lista=[]#Se declara una variable para para guardar la lista
    for x in range(0,10000):#cantidad de palabras
      x=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(0,12))#num caracteres
      lista.append(x)#append es propiedad que ingresa los datos a la lista
    return lista

  #Crear archivo con el nombre
  def crearArchivo(self, nombre):
    self.nombre = nombre
    archivo=open(f"{self.nombre}.txt",'w')#f"{self.nombre}//manera de concatenar str, 'w' para crear y escribir
    archivo.close()

  #Escribir archivo con el nombre
  def escribir(self):
    archivo=open(f"{self.nombre}.txt",'a')#'a' para escribir al utlimo y crear archivo
    for i in self.random_caracter():#Se utiliza para imprimir las palabras del retorno del metodo random_caracter 
      archivo.write(i+' ')



