class Perro:
    def habla(self):  # Esto ya es un 'metodo', que una función dentro de una clase
        print('guau!!!')


mi_perro = Perro()

# print(type(mi_perro))
mi_perro.habla()
print(isinstance(mi_perro, Perro))
