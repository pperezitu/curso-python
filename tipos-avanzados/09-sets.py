# set significa grupo o conjunto

primer = {1, 1, 2, 2, 3, 4}
# primer.add(5)
# primer.remove(1)
# print(primer)

segundo = [3, 4, 5, 6]
segundo = set(segundo)

print(primer | segundo)  # este simbolo | es un operador y se le conoce com union!
print(primer & segundo)
print(primer - segundo)
print(primer ^ segundo)

if 5 in segundo:
    print('Hola mundo!!!')
    