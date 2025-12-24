texto = 'Hello World \nEsto es un poco de texto\nQue tengas un buen dia!'

with open('test2.txt','w') as file:#el w es para writing y a es para add texto
    file.write(texto)

with open('test2.txt') as file:
    print(file.read())