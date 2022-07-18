import os 

class Search:

    #Busca el numero de coincidencias de la palabra insertada en el metodo
    #archivo: Nombre del archivo
    #content: La palabra que debe ser buscada 
    def buscarCoincidencias(self,archivo,content):
        
        archivoAbierto = os.open(f"./{archivo}.txt",flags = os.O_RDWR | os.O_CREAT)
        os.lseek(archivoAbierto, 0, 0)
        str = os.read(archivoAbierto, os.path.getsize(archivoAbierto))
        numeroCoincidencias=str.decode().count(content)
        os.close(archivoAbierto)

        return numeroCoincidencias




