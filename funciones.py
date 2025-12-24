def saludo(primer_nombre, apellido, edad):
    print('Hola ' + nombre + ' ' + apellido)
    print('Tienes '+ str(edad) + ' años')
    print('que tengas un buen dia!')

#nombre = 'Alex'
nombre = input('Introduce tu nombre: ')
saludo(nombre, 'Smith', 23)