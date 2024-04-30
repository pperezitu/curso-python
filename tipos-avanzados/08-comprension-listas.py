# usuarios = [
#     [4, 'Lucia'],
#     [2, 'Diana'],
#     [7, 'Morito']
# ]

usuarios = [
    ['Lucia', 8],
    ['Diana', 1],
    ['Morito', 12]
]

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[1])
# print(nombres)

# map
# nombres = [usuario[1] for usuario in usuarios]
# print(nombres)


# nombres = list(map(lambda usuario: usuario[1], usuarios))
# print(nombres)

menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)
