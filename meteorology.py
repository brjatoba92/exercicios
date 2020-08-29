serie_meteorologica = []

posicao_inicial = 1

while posicao_inicial > 0:
    print("Temperatura", posicao_inicial)
    temperatura = serie_meteorologica.append(float(input('Registre a temperatura: ')))
    posicao_inicial += 1

    x = str(input('Digite e para encerrar ou c para continuar: '))
    if x == "e":
        break
    elif x == "c":
        continue

media = sum(serie_meteorologica) / len(serie_meteorologica)
maior = max(serie_meteorologica)
menor = min(serie_meteorologica)

print("Registro da temperatura" )
print("Media da temperatura", media, "°C")
print("Temperatura maxima",  maior, "°C")
print("Temperatura minima",  menor, "°C")