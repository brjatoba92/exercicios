"""
PROGRAMA NUMEROS IMPARES

- Numeros impares quando dividido por 2 o resto é maior que 0

"""

numero = int(input('Digite um  numero: '))

if 1 <= numero <= 50:
    if numero % 2 > 0: 
        print('Este numero é impar')
    else:
        print('Este numero é par')
else:
    pass