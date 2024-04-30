# numeros = (1, 2, 3, 4)
numeros = (1, 2, 3, 4) + (5, 6, 7)

print(numeros)

punto = [1, 2]

punto = tuple([1, 2])
print(punto)

menosNumeros = numeros[:2]
print(menosNumeros)

primero, segundo, *otros = numeros
print(primero, segundo, otros)

for n in numeros:
    print(n)


listaNumeros = list(numeros)
listaNumeros[0] = 'Chanchito Feliz'
print(listaNumeros)
