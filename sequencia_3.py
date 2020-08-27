numero_1 = int (input('Primeiro numero: '))
numero_2 = int (input('Segundo numero: '))

sequencia = list(range(numero_1, numero_2 + 1)) 

print(sequencia)

"""
SOMAR OS ELEMENTOS DA SEQUENCIA

"""

for i in range (numero_1 + 1, numero_2): #Para valores de i contido no range faça até o numero 2
    print (i)

for i in range(numero_2 + 1, numero_2):
    print (i)

print("Soma dos números contidos na lista: ", i+i)
