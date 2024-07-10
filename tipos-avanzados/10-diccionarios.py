punto = {'x': 25, 'y': 50}
print(punto)
print(punto['x'])
print(punto['y'])

punto['z'] = 45
if 'lala' in punto:
    print('encontre lala', punto['lala'])
    
print(punto.get('x'))
print(punto.get('lala', 97))
del punto['x']
del (punto['y'])
# print(punto)

for valor in punto:
    print(valor)


usuarios = [
    {"id": 1, "nombre": "Lucia"},
    {"id": 2, "nombre": "Diana"},
    {"id": 3, "nombre": "Benito"},
]

for usuario in usuarios:
    print(usuario["nombre"])