"""
PROGRAMA SEQUENCIA DE NUMEROS

- Cria lista de 1 a 20
- Imprime numeros na vertical
"""

numero = list(range(1,21))

print(numero)

#print(numero[0])
#print(numero[19])

i = 0 #Primeiro elemento da lista
while numero[i] < numero[19]: #Enquanto numero[i] (1) for menor que numero[19] faça:
    i += 1 #acrescentar de 1 em 1
    j = numero[0] + i #numero seguinte acrescenta i (1)
    print(i)
    print(j)
