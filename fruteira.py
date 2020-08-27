"""
PROGRAMA FRUTEIRA
"""

morango = int(input('Quantidade de kg do morango: '))
maca = int(input('Quantidade de kg: da maçã: '))

#morango

if morango <= 5:
    preco_morango = morango * 2.5
else:
    preco_morango = morango * 1.8

#maçã

if maca > 5:
    preco_maca = maca * 2.2
else:
    preco_maca = maca * 1.5

#Desconto maior

if preco_morango > 25 and preco_maca > 25:
    preco_morango_2 = preco_morango * 0.75
    preco_maca_2= preco_maca * 0.75
    print(preco_morango_2, preco_maca_2)
else:
    print(preco_morango, preco_maca)