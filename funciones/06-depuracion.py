def largo(texto):
    resultado = 0
    for _ in texto:
        resultado += 1
    return resultado


print('Lucia feliz en el dentista')
l = largo('Hola mundo')
print(l)
