print('Bienvenidos a calculadora')
print('Para salir escribe "salir"')
print('Las operaciones son suma, resta, multiplicar y dividir!')

resultado = ''
while True:
    if not resultado:
        resultado = input('Ingrese número: ')
        if resultado.lower() == 'salir':
            break
        resultado = int(resultado)
    op = input('Ingresa opereación: ')
    if op.lower() == 'salir':
        break
    n2 = input('ingrese el siguiente número: ')
    if n2.lower() == 'salir':
        break
    n2 = int(n2)
    
    if op.lower() == 'suma':
        resultado += n2
    elif op.lower() == 'resta':
        resultado -= n2
    elif op.lower() == 'multiplicacion':
        resultado *= n2
    elif op.lower() == 'division':
        resultado /= n2
    else:
        print('Operación no válida')
        break
    
    print(f'El resultado es {resultado}')
    