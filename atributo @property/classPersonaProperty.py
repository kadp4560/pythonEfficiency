class Perros:

    def __init__(self, nombre, peso):
        self.__nombre = nombre # Definir los atributos privados ocultos.
        self.__peso   = peso
    
    @property
    def nombre(self):

        "Documentación del método de nombre bla bla bla" # Doc del método 
        return self.__nombre #Retorno del atributo oculto.

#Hasta aquí definimos los métodos para obtener los atributos ocultos o privados getter.
#Ahora vamos a utilizar setter y deleter para modificarlos

    @nombre.setter #Propiedad SETTER
    def nombre(self, nuevo):
        print("Modificando nombre... ")
        self.__nombre = nuevo
        print(" El nombre se ha modificado por: ")
        print(self.__nombre) # Retorno del atributo para confirmar.
    
    @nombre.deleter #Propiedad DELETER
    def nombre(self):
        print("Borrando nombre")
        del self.__nombre
    
    @property
    def peso(self):	#Definimos el método para obtener el
        return self.__peso #Aquí simplemente estamos retornando el atributo privado
    
    @peso.setter
    def peso(self, nuevo):
        print("Modificando peso... ")
        self.__peso = nuevo
        print(" El peso se ha modificado por: ")
        print(self.__peso) # Retorno del atributo para confirmar.
    
    @peso.deleter
    def peso(self):
        print("Deleting peso... ")
        del self.__peso





perro1 = Perros("Ponky",70)
print (perro1.nombre)
perro1.nombre = "Ponke"

del perro1.nombre

print (perro1.peso)
perro1.peso = 80

del perro1.peso

