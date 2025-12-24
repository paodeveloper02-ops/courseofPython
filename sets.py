utensilios = {'tenedor', 'cuchara', 'cuchillo'} #set no repite elementos
platos = {'plato','bol','taza','cuchara'}

utensilios.add('cucharita')
#utensilios.remove('cuchara')
#utensilios.pop()#elimina un elemento al azar
utensilios.update(platos) #agrego platos a utensilios

print(utensilios.difference(platos))
print(utensilios.intersection(platos))
for x in utensilios:
    print(x + ' ',end='')