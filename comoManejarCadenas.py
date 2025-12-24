nombre = 'Paola Moreno'
primer_nombre = nombre[0:5]#el 5 es exclusivo,el 0 es inclusivo,el 5 es para contar hasta el 4to letra
apellido = nombre[6:12]
apellido2 = nombre[6:]#imprime hasta el final de la cadena
print(primer_nombre)
print(apellido)
print(apellido2)
nombre_dos = nombre[0:12:1]
print(nombre_dos)
nombre_invertido = nombre[::-1]
print(nombre_invertido)
nombre_invertido2 = nombre_invertido[::-1]
print(nombre_invertido2)

website = 'http://www.wikipedia.com'
slice = slice(11,-4)
sitio = website[slice]
print(sitio)