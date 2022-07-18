from ArchivoRandom import ArchivoRandom
from Search import Search

 #El atributo self es propio de el metodo, para usar los metodos primero se instancia en una varibale(Crear objeto)
 #

class Main:
    
    #Instancias de las clases ArchivoRandom,Search
    __archivo= ArchivoRandom()
    __search= Search()  

    def __init__(self):
        pass

    #Genera un archivo con el nombre insertado en el metodo
    #En el nombre del  archivo no debe incluir la extension simplemente ingrese el nombre del archivo.
    def archivoRandom(self,nombre):
        self.__archivo.crearArchivo(nombre)
        self.__archivo.escribir()

    #Busca las coincidencias de la palabra
    #En el nombre del  archivo no debe incluir la extension simplemente ingrese el nombre del archivo
    def buscarPalabra(self,nombreArchivo,palabra):
        return self.__search.buscarCoincidencias(nombreArchivo,palabra)


#Ejemplo de uso
#Se recomienda hacer una interfaz que permite al usuario ingresar el los atributos del metodo
main = Main()

main.archivoRandom("globo")
answer =main.buscarPalabra("globo","hola")
print (answer)
