import random

x = random.randint(1,100)#numero aleatorio entre 1 y 100
y = random.random() #numero aleatorio entre 0 y 1

mi_lista = ['Piedra','Papel','Tijera']
z = random.choice(mi_lista)#elijo una opcion random de mi lista

cartas = ['1','2','3','4','5','6','7','8','9','J','Q','K','A']
random.shuffle(cartas)#cambio posicion de las cartas,o sea el orden
print(cartas)
print(z)