"""
JOGO TOPA OU NÃO TOPA

"""
quantidade_maletas = 10

maleta_1milhao = 5
maleta_10mil = 1
maleta_20mil = 2
maleta_50mil = 3
maleta_500mil = 4

maleta_escolhida = int(input('Digite sua maleta: '))

while maleta_escolhida < quantidade_maletas:
    maleta_escolhida = int(input('Digite sua maleta: '))
else:
    print('Parabens, voce ganhou um milhão!!!!!')
