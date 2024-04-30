numeros = [21, 2, 31, 4, 52, 6, 7, 8, 29]

# numeros.sort()
numeros.sort(reverse=True)
print(numeros)

usuarios = [
    [4, 'Lucia'],
    [2, 'Diana'],
    [7, 'Morito']
]


# def ordenar(elemento):
#     return elemento[1]
#
#
# usuarios.sort(key=ordenar)
# print(usuarios)


usuarios.sort(key=lambda el: el[1], reverse=True)
print(usuarios)
