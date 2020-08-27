"""
PROGRAMA QUANTIDADE NUMEROS PARES E IMPARES

- Define valor de 0 para numero impar
- Define valor 1 para numero par
"""

numero_1 = int(input('Informe um numero: '))
numero_2 = int(input('Informe um numero: '))
numero_3 = int(input('Informe um numero: '))
numero_4 = int(input('Informe um numero: '))
numero_5 = int(input('Informe um numero: '))
numero_6 = int(input('Informe um numero: '))
numero_7 = int(input('Informe um numero: '))
numero_8 = int(input('Informe um numero: '))
numero_9 = int(input('Informe um numero: '))
numero_10 = int(input('Informe um numero: '))

if numero_1 % 2 == 0:
    x_1 = 1
else:
    x_1 = 0
    
if numero_2 % 2 == 0:
    x_2 = 1
else:
    x_2 = 0
    
if numero_3 % 2 == 0:
    x_3 = 1
else:
    x_3 = 0
    
if numero_4 % 2 == 0:
    x_4 = 1
else:
    x_4 = 0
    
if numero_5 % 2 == 0:
    x_5 = 1
    
else:
    x_5 = 0
    
if numero_6 % 2 == 0:
    x_6 = 1
else:
    x_6 = 0
    
if numero_7 % 2 == 0:
    x_7 = 1
else:
    x_7 = 0
    
if numero_8 % 2 == 0:
    x_8 = 1  
else:
    x_8 = 0
    
if numero_9 % 2 == 0:
    x_9 = 1 
else:
    x_9 = 0
    
if numero_10 % 2 == 0:
    x_10 = 1
else:
    x_10 = 0

soma = x_1 + x_2 + x_3 + x_4 + x_5 + x_6 + x_7 + x_8 + x_9 + x_10 #0 para impar e 1 para par

if soma == 10:
    print('10 numeros pares')
elif soma == 0:
    print('10 numeros impares')
elif soma == 1:
    print('9 impares e 1 par')
elif soma == 2:
    print('8 impares e 2 pares')
elif soma == 3:
    print('7 impares e 3 par')
elif soma == 4:
    print('6 impares e 4 pares')
elif soma == 5:
    print('5 impares e 5 pares')
elif soma == 6:
    print('4 impares e 6 pares')
elif soma == 7:
    print('3 impares e 7 pares')
elif soma == 8:
    print('2 impares e 8 pares')
elif soma == 8:
    print('1 impar e 9 pares')

#Forma curta

matriz_valor = [numero_1, numero_2, numero_3, numero_4,  numero_5, numero_6, numero_7, numero_8, numero_9, numero_10]

par = 0
impar = 0

for valor in matriz_valor:
    if valor % 2 ==0:
        #print('par')
        par = par + 1
    else:
        #print('impar')
        impar = impar + 1

print("Quantidade de numeros impares:", impar, "Quantidade de numeros pares:", par)
    