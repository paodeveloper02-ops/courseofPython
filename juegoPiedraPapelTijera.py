import random

lista = ['piedra', 'papel', 'tijera']

while True:
    jugador = None
    computadora = random.choice(lista)

    while jugador not in lista:
        jugador = input('piedra, papel o tijera?: ').lower()

    print('Computadora:', computadora)
    print('Jugador:', jugador)

    if computadora == jugador:
        print('Empate')
    elif jugador == 'tijera':
        if computadora == 'piedra':
            print('Perdiste')
        else:
            print('Ganaste')
    elif jugador == 'piedra':
        if computadora == 'papel':
            print('Perdiste')
        else:
            print('Ganaste')
    elif jugador == 'papel':
        if computadora == 'tijera':
            print('Perdiste')
        else:
            print('Ganaste')

    jugar_de_nuevo = input('¿Quieres jugar de nuevo (si/no)?: ').lower()
    if jugar_de_nuevo != 'si':
        break

print('Adiós')
