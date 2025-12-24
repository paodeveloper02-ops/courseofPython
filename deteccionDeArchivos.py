import os

path = 'C:\\Users\\User\\Desktop\\courseofPython'

if os.path.exists(path):
    print('Esa ubicación existe!')
    if os.path.isdir(path):
        print('Este es un directorio')

    elif os.path.exists(path):
        print('Es un archivo existente')
else:
    print('Esa ubicacion no existe!')

