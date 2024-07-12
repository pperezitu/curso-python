# diferencias entre propiedades de clase y propiedades de instancia
class Perro:

    def __init__(self, nombre, edad):  # este es el constructor
        # print(nombre)
        self.__nombre = nombre
        self.edad = edad
        
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self):
        return self.__nombre

    def habla(self):  # Esto ya es un 'metodo', que una función dentro de una clase
        print(f'{self.__nombre} dice: Guau!!!')

    @classmethod
    def factory(cls):
        return cls('Diana contenta', 4)


perro1 = Perro.factory()
perro1.habla()
perro1.get_nombre()