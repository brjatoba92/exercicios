"""
PROGRAMA VALOR MAIOR/MENOR/SOMA DOS VALORES DE UMA LISTA

- SOMAR OS VALORES DA LISTA
- MAIOR VALOR DE UMA LISTA ==> max
- MENOR VALOR DE UMA LISTA ==> min
- LIMITAR SE OS VALORES DA LISTA FOR ENTRE 0 E 1000
"""

numero = int(input('Teste: ')) #define a quantidade de numeros em uma lista

if 0 < numero <= 1000:
    i = 0 
    z = range(numero+1) #lista

    for valor in range(numero+1):
        i += valor
    print(i) #imprime a soma dos valores da lista
    x = max(z) #valor maximo da lista
    y = min(z) #valor minimo da lista
    print(x)
    print(y)

else:
    pass
