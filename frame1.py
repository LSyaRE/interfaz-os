from os_archivos.main import Main
import os

class Frame1:
    __archivo = Main()

    def __init__(self):
        pass

    def crearArchivo(self):
        return self.__archivo.archivoRandom('hola')

    def leerArchivo(self):
        archivoAbierto = os.open(f"./hola.txt",flags = os.O_RDWR | os.O_CREAT)
        os.lseek(archivoAbierto, 0, 0)
        str = os.read(archivoAbierto, os.path.getsize(archivoAbierto))
        res = str.decode() 
        os.close(archivoAbierto)
        return res
        
