nombre = 'paola Moreno!'

if nombre[0].islower():
    nombre = nombre.capitalize()

primer_nombre = nombre[:5].upper()
apellido = nombre[6:-1].lower()
ultimo_caracter = nombre[-1]

print(primer_nombre)
print(apellido)
print(ultimo_caracter)