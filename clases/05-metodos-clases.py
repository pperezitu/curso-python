# diferencias entre propiedades de clase y propiedades de instancia
class Perro:
    patas = 4
    
    def __init__(self, nombre, edad):  # este es el constructor
        # print(nombre)
        self.nombre = nombre
        self.edad = edad
        
    @classmethod
    def habla(cls):  # Esto ya es un 'metodo', que una función dentro de una clase
        print('Guau!!!')
        
    @classmethod
    def factory(cls):
        return cls('Diana contenta', 4)
        
Perro.habla()
perro2 = Perro.factory()
print(perro2.edad, perro2.nombre)
