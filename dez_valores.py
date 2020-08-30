"""
CLIENTES ALTURAS
- LIMITA A 10 ENTRADAS
- VALOR MAXIMO E MINIMO DAS ALTURAS
"""

aluno_codigo = []
aluno_altura = []

i = 1

while i <= 10:
    print("Cliente", i)
    codigo = int(input('Digite seu codigo: '))
    altura = int(input('Digite sua altura (cm): '))
    lista_codigo = aluno_codigo.append(codigo)
    lista_altura = aluno_altura.append(altura)
    i += 1
    x = str(input('Digite e para encerrar ou c para continuar: '))
    if x == "e":
        break
    elif x == "c":
        continue

"""
cod_gordo = cliente_peso.index(max(peso))
cod_magro = cliente_peso.index(min(peso))
cod_alto = cliente_altura.index(max(altura))
cod_baixo = cliente_altura.index(min(altura))
"""

print("Menor altura: ", min(aluno_altura))
print("Maior altura: ", max(aluno_altura))