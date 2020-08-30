"""
PROGRAMA SOLUCIONE SUAS DIVIDAS
- INFORMAR DIVIDA INICIAL
- JUROS PADRÃO DE 10%(3 PARCELAS), AUMENTANDO DE 5% A CADA TRES PARCELAS(6 = 15%, 9 = 20%, 12 = 25%)
- CALCULO DO VALOR DO JUROS
- INFORMA O VALOR FINAL
- INFORMA A QUANTIDADE DE PARCELAS
- INFORMA O VALOR DE CADA PARCELA
"""

print("Bom dia. Bem vindo ao SOLUCIONE SUAS DIVIDAS")
divida_inicial = int(input('Digite sua divida'))
quantidade_parcelas = int(input('Digite o numero maximo de parcelas (3x, 6x, 9x e 12x)'))
juros_inicial = 0.1

i = 1


print("Você tem as seguintes opções de parcelamento")
while i <= quantidade_parcelas:
    i += 1
    if i == 2:
    #divida_final = divida_inicial
        print("Parcela", i-1, "Valor:", divida_inicial)
    if i == 4:
        print("Valores acrescidos de juros:")
        juros = juros_inicial
        valor_juros = (divida_inicial * (juros))
        print("Parcela", i-1, "Valor de juros:", valor_juros)
        divida_final = divida_inicial + valor_juros
        print("Divida:",divida_final)
        parcela = divida_final / (i-1)
        print("Valor de cada parcela:", parcela)

    elif i == 7:
        juros = juros_inicial + 0.05
        valor_juros = (divida_inicial * (juros))
        print("Parcela", i-1, "Valor de juros:", valor_juros)
        divida_final = divida_inicial + valor_juros
        print("Divida:",divida_final)
        parcela = divida_final / (i-1)
        print("Valor de cada parcela:", parcela)

    elif i == 10:
        juros = juros_inicial + 0.10
        valor_juros = (divida_inicial * (juros))
        print("Parcela", i-1, "Valor de juros:", valor_juros)
        divida_final = divida_inicial + valor_juros
        print("Divida:",divida_final)
        parcela = divida_final / (i-1)
        print("Valor de cada parcela:", parcela)

    elif i == 13:
        juros = juros_inicial + 0.15
        valor_juros = (divida_inicial * (juros))
        print("Parcela", i-1, "Valor de juros:", valor_juros)
        divida_final = divida_inicial + valor_juros
        print("Divida:",divida_final)
        parcela = divida_final / (i-1)
        print("Valor de cada parcela:", parcela)
    
     #implementar os valores das parcelas mediante   