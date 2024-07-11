class Perro:
    def __init__(self, nombre, edad):  # este es el constructor
        # print(nombre)
        self.nombre = nombre
        self.edad = edad
        
    def habla(self):  # Esto ya es un 'metodo', que una función dentro de una clase
        print(f'{self.nombre} dice: Guau!!!')


mi_perro = Perro('Morito', 2)
mi_perro.habla()
print(mi_perro.nombre, mi_perro.edad)