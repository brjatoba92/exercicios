cliente_codigo = []
cliente_nome = []
cliente_altura = []
cliente_peso = []

i = 1

while i > 0:
    #print("Temperatura", i)
    print("Cliente", i)
    nome = str(input('Digite seu nome: '))
    codigo = int(input('Digite seu codigo: '))
    altura = float(input('Digite sua altura (cm): '))
    peso = float(input('Digite seu peso (kg): '))
    lista_nome = cliente_nome.append(nome)
    lista_codigo = cliente_codigo.append(codigo)
    lista_altura = cliente_altura.append(altura)
    lista_peso= cliente_peso.append(peso)
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

print("Clientes: ", cliente_nome)
print("Codigos: ", cliente_codigo)
print("Menor peso: ", min(cliente_peso))
print("Menor altura: ", min(cliente_altura))
print("Maior peso: ", max(cliente_peso))
print("Maior altura: ", max(cliente_altura))
print("Media do peso: ", sum(cliente_peso) / len(cliente_peso))
print("Media da altura: ", sum(cliente_altura) / len(cliente_altura))
