lista=[1]
print(lista*4)


lista=['frutras','candies','sal']
listas= list(enumerate(lista,2019))
print(list(enumerate(lista,2019)))


print(type(listas[0]))


class Estudiante(object):
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad
  
  def presentacion(self):
    return"Hola mi nombre es %s y tengo %i años" %(self.nombre, self.edad)
e = Estudiante("Arturo", 21)
print(e.presentacion())