"""
ESTATISTICA ACIDENTES DE TRANSITOS
"""

codigo_cidade = []
numero_veiculos = []
numero_acidentes = []

i = 1

while i > 0:
    cidade = str(input('Digite o codigo da cidade: '))
    veiculos = int(input('Digite o numero de veiculos: '))
    acidentes = int(input('Digite o numero de acidentes: '))
    lista_codigos = codigo_cidade.append(cidade)
    lista_veiculos = numero_veiculos.append(veiculos)
    lista_acidentes = numero_acidentes.append(acidentes)
    i +=1 

    if acidentes == max(numero_acidentes):
        maior_acidentes = cidade
    elif acidentes == min(numero_acidentes):
        menor_acidentes = cidade

    x = str(input('Digite e para encerrar ou c para continuar: '))
    if x == "e":
        break
    elif x == "c":
        continue

print("Codigos das cidades: ", codigo_cidade)
print("Numero de veiculos: ", numero_veiculos)
print("Numero de acidentes: ", numero_acidentes)
print("Cidade: ", maior_acidentes,".", "Maior valor de acidentes de transitos", max(numero_acidentes))
print("Cidade: ", menor_acidentes,".", "Menor valor de acidentes de transitos", min(numero_acidentes))
print("Media de veiculos", sum(numero_veiculos) / len(numero_veiculos))
print("Media dos acidentes de transitos", sum(numero_acidentes) / len(numero_acidentes))


