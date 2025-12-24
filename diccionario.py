capitales = {
    'EE.UU': 'Washington D.C',
    'Argentina': 'Buenos Aires',
    'Chile': 'Santiago de Chile',
    'Brasil': 'Brasilia',
    'cursos': ['Python', 'C++'],
    'años':23
}
#print(capitales['Chile'])
#print(capitales.get('Alemania'))
print(capitales.keys())
print('ahora voy a traer los valores de las llaves')
print(capitales.values())
print('ahora voy a traer los valores completos')
print(capitales.items())
print('ahora voy a agregar alemania')
capitales.update({'Alemania': 'Berlin'})
print('ahora voy a recorrer el diccionario con su llave y su valor')
print('ahora voy a eliminar estados unidos')
capitales.pop('EE.UU')
#print('ahora voy a eliminar todas las capitales')
#capitales.clear()
for key, value in capitales.items():
    print(key,value)