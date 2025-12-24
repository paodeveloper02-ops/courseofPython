import os
#path = 'test3.txt' esto es para eliminar archivo
#try:
#    os.remove(path)
#except FileNotFoundError:
#    print('El archivo no se encontró!')
import shutil
path = 'folder'
try:
    #os.remove(path)
    #os.rmdir(path)#rmdir es para eliminar directorios o sea carpeta vacias
 shutil.rmtree(path) #para eliminar carpetas no vacias
except FileNotFoundError:
   print('El archivo no se encontró!')
except PermissionError:
    print('No tienes permiso para eliminar esta carpeta')
except OSError:
    print("No puedes eliminar eso usando esa función")

else:
    print("Path fue eliminado")
