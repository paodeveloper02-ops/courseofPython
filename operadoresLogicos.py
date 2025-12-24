temperatura = int(input('Ingrese la temperatura: '))

if not(temperatura >= 0 and temperatura <= 30):
    print('La temperatura esta mal hoy.Quedate adentro!')
elif not(temperatura < 0 or temperatura > 30):
    print('La temperatura esta bien hoy. Sal afuera!')

if temperatura >= 0 and temperatura <= 30:
    print('La temperatura esta bien hoy.Sal afuera!')
elif temperatura < 0 or temperatura > 30:
    print('La temperatura esta mal hoy.Quedate adentro!')