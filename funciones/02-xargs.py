# def suma(a, b):
#     print(a + b)
# 
# 
# suma(2, 4)

def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(12, 3, 7, 22)
suma(2, 3, 4, 6)
