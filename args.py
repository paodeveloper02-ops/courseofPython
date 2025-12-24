def suma(*cosas): #al usar * es una tupla de objetos o int en este caso
    suma = 0
    cosas = list(cosas)
    cosas[0] = 0
    for i in cosas:
        suma += i
    return suma

print(suma(2,3,8))

def suma(*args):
    suma = 0
    for i in args:
        suma += i
    return suma
print(suma(1,5,3))