"""
AUMENTO DE SALARIO ANUALMENTE
"""
salario_inicial = 1000
taxa = 0.015
ano_inicial = 1995

i = 1

while i > 0:
    #print("Ano:", ano_inicial, "Salario inicial:", salario_inicial)
    ano_final = ano_inicial + i
    salario_atual = salario_inicial * (1 + i * taxa)
    print("Ano:", ano_final, "Salario atual:", salario_atual)
    i += 1

    x = str(input('Digite e para encerrar ou c para continuar: '))
    if x == "e":
        break
    elif x == "c":
        continue

