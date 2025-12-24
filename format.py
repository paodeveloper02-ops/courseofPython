#str.format() =
str_1 = 'leche'
str_2 = 'casar'

#print('Arroz con leche me quiero casar')
#print('Arroz con '+ str_1 + ' me quiero ' + str_2)
#print('Arroz con {} me quiero {}'.format('leche','casar'))
#print('Arroz con {} me quiero {}'.format(str_1,str_2))
#print('Arroz con {1} me quiero {0}'.format(str_1,str_2))#ponemos el indice de los parametros entre llaves
#print('Arroz con {str_1} me quiero {str_2}'.format(str_1='leche',str_2='casar'))

#texto = 'Arroz con {} me quiero {}'
#print(texto.format(str_1, str_2))

nombre = 'Paola'
#print('Hola, mi nombre es: {}'.format(nombre))
print('Hola, mi nombre es: {:10}. Mucho gusto :D'.format(nombre))
print('Hola, mi nombre es: {:<10}. Mucho gusto :D'.format(nombre))
print('Hola, mi nombre es: {:>10}. Mucho gusto :D'.format(nombre))
print('Hola, mi nombre es: {:^10}. Mucho gusto :D'.format(nombre))

numero = 3.14159

print('El numero PI es: {:.2f}'.format(numero))