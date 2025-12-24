import os

origen = 'folder'
destino = 'C:\\Users\\User\\Desktop\\folder'

try:
    if os.path.exists(destino):
        print('Ya hay un archivo en este destino')
    else:
        os.replace(origen, destino)#los mueve de carpeta
        print(origen + ' fue movido')
except FileNotFoundError:
    print(origen + 'no fue encontrado')

