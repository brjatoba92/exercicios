limite = int(input('Digite o valor limite: '))
serie_nprimo = []

for primo in range(limite + 1):
    if primo > 5 and primo % 5 == 0:
        pass
    elif primo % 2 == 1 and primo > 2: #numeros impares
        serie_nprimo.append(primo)

print(serie_nprimo)