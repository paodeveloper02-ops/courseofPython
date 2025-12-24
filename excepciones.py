try:
    numerador = int(input('Ingresa un número: '))
    denominador = int(input('Ingresa un número: '))
    resultado = numerador / denominador

except ZeroDivisionError as e:
    print (e)
    print('No puedes dividir por 0')
except ValueError as e:
    print (e)
    print('Por favor, ingresa solo numeros')
except Exception as e:#puedo poner soolo except esxception:
    print (e)
    print('Algo salió mal')
else:
    print(resultado)
finally:
    print('Esto se ejecuta siempre')