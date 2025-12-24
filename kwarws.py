def hola(**nombre): #diccionario que empaqueta palabras
    #print('Hola ' + kwargs['nombre'] + ' ' + kwargs['apellido'])
    print('Hola',end = ' ')
    for calve,valor in nombre.items():
        print(valor,end = ' ')

hola(titulo = 'Señora',nombre = 'Paola', apellido = 'Moreno',segundo_nombre = 'Python')