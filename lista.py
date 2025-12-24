comida = ['Pizza', 'Hamburguesa', 'Hot Dog', 'Espaguetis', 2 , 0.5 , False]

comida.append('Pudding')#agrego un elemento al final de la lista
print(comida)
print(comida[0])
comida.remove('Pizza')#elimino el elemento
comida.pop()#elimino ultimo elemento de la lista
comida.insert(0,'Pastel')#agrego en eleemento en posicion 0
comida.sort()#ordeno alfabeticamente

for x in comida:
    print(x + ',',end="")

comida.clear()#vacio la lista
print(comida)