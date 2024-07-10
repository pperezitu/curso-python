lista = [1, 2, 3, 4]
lista2 = [5, 6, 7]

combinada = ['Hola ', *lista, 'Lucia', *lista2, 'esta feliz!']
print(combinada)


punto1 = {'x': 19}
punto2 = {'y': 17}

nuevoPunto = {**punto1, **punto2}
print(nuevoPunto)
