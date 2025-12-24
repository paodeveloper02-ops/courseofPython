try:
    with open('test.txt') as file:
        print(file.read())

#print(file.closed)
except FileNotFoundError:
    print('El archivo no fue encontrado')
