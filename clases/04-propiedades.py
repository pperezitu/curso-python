# diferencias entre propiedades de clase y propiedades de instancia
class Perro:
    patas = 4
    def __init__(self, nombre, edad):  # este es el constructor
        # print(nombre)
        self.nombre = nombre
        self.edad = edad
        
    def habla(self):  # Esto ya es un 'metodo', que una función dentro de una clase
        print(f'{self.nombre} dice: Guau!!!')


mi_perro = Perro('Morito', 2)
Perro.patas = 3
mi_perro2 = Perro('Diana', 5)
mi_perro.habla()
print(mi_perro.nombre, mi_perro.edad)
print(Perro.patas)
mi_perro2.patas = 5
print(mi_perro2.patas)
