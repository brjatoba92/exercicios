#PROGRAMA LOJA DE TINTAS

#1 litro para cada 3 m2
# latas de 18 litros
# custo por lata 80 reais

area = int(input('Digite a area a ser pintada:'))

litros = area / 3

quantidade_de_latas = (litros / 18)
valor_total = (quantidade_de_latas * 80)

print ('Quantidade de latas a serem compradas:')
print (quantidade_de_latas)
print ('Valor a ser pago: ')
print (valor_total)


#LOJAS DE TINTAS 2

"""
By Bruno Jatoba

O programa solicita o tamanho da area necessaria e disponibiliza 3 opções:

- Latas:
a) 1 litro cobre 6 metros quadrados
b) 1 lata = 18 litros
c) Custo de 80 reais por lata

- Galão
a) 1 litro = 6 metros quadrados
b) 1 galão = 3.6 litros 
c) Custo de 25 reais por galão

- Latas e galão #implementar
a) Mistura de latas e galões
b) Evitar desperdicio - acrescente 10% de folga
c) latas cheias
"""

def pagina_inicial():
    print ('Bem vindo a Feliz Tintas:')
    print ('1. Latas de 18 litros')
    print ('2. Galões de 3.6 litros')
    print ('3. Latas e galões')


def latas_tintas():
    area = float(input ('Digite a area necessaria: '))
    litros_latas = area / 6
    quantidade_latas = (litros_latas / 18)
    valor_latas = (quantidade_latas * 80)
    print ('Quantidade de latas a serem compradas:')
    print (quantidade_latas)
    print ('Valor a ser pago:')
    print (valor_latas)

def galoes_tintas():
    area = float(input ('Digite a area necessaria: '))
    litros_galoes = area / 6
    quantidade_galoes = (litros_galoes / 3.6)
    valor_galoes = (quantidade_galoes * 25)
    print ('Quantidade de galões a serem compradas:')
    print (quantidade_galoes)
    print ('Valor a ser pago:')
    print (valor_galoes)

def latas_galoes():
    area = float(input ('Digite a area necessaria: '))
    litros_latas = area / 6
    litros_galoes = area / 6
    quantidade_latas = (litros_latas / 18)
    quantidade_galoes = (litros_galoes / 3.6)
    quantidade_total = quantidade_latas + quantidade_galoes
    valor_latas = (quantidade_latas * 80)
    valor_galoes = (quantidade_galoes * 25)
    valor_total = valor_latas + valor_galoes
    print ('Quantidade de latas e galões a serem compradas:')
    print (quantidade_total)
    print ('Valor a ser pago:')
    print (valor_total)

if __name__ == "__main__":
    pagina_inicial()
    opcao = input ('Escolha a opção:')

    if opcao == '1':
        latas_tintas()
    
    if opcao == '2':
        galao_tintas()
    
    if opcao == '3':
        latas_galoes()

