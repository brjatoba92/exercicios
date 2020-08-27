"""
PROGRAMA POPULACÃO DE PAISES DIFERENTES
- Define uma condição de loop (while) mostre valores das populações (A menor/igual a B) e finaliza quando A for maior que B
"""

populacao_a = 80000
populacao_b = 200000

taxa_a = 1.03
taxa_b = 1.015

i = 0 

while populacao_a <= populacao_b:
    i += 1 #acrescentar 1 ano no loop e finaliza quando a condição acima for atingida
    populacao_a = populacao_a * taxa_a
    populacao_b = populacao_b * taxa_b
    print("São necessarios %i anos para a populacao do pais A superar a do pais B." % i) #indica a quantidade de anos
    print("Pais A: %.0f" % populacao_a) #mostra a populacão quando atingir o ano limite para que A for maior que B
    print("Pais B: %.0f" % populacao_b)


"""
PROGRAMA POPULACÃO DE PAISES DIFERENTES 2
 
- Define uma condição de loop (while) mostre valores das populações (A menor/igual a B) e finaliza quando A for maior que B
"""

populacao_a = int(input('População A'))
populacao_b = int(input('População B'))

taxa_a = float(input('Taxa A'))
taxa_b = float(input('Taxa B'))

i = 0 

while populacao_a <= populacao_b:
    if i < 1000:
        i += 1 #acrescentar 1 ano no loop e finaliza quando a condição acima for atingida
        populacao_a = populacao_a * taxa_a
        populacao_b = populacao_b * taxa_b
        print("São necessarios %i anos para a populacao do pais A superar a do pais B." % i) #indica a quantidade de anos
        print("Pais A: %.0f" % populacao_a) #mostra a populacão quando atingir o ano limite para que A for maior que B
        print("Pais B: %.0f" % populacao_b)
