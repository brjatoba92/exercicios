""" MENU DE OPÇÕES """

def pagina_secundaria():
    print ('1. Frutas')
    print ('2. Carnes')

"""
MODULO SUPERMERCADO/FRUTEIRA
- Informa o peso de frutas diferentes
- Calcula o preço
- Desconto quando passa de 25 kg
"""

def frutas():
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

"""
MODULO SUPERMERCADO/CARNES

- Definir os valores dos produtos

- Definir os valores em função dos tipos de produtos e da quantidade de quilos

- Definir se o cliente comprou ou não no cartão:
  - Se sim recebe um desconto de 5% no total da compra
  - Se não, o valor e a soma dos produtos
"""

def carnes ():
    contrafile = int(input('Quantidade de kg do Contra File: '))
    alcatra = int(input('Quantidade de kg da Alcatra: '))
    picanha = int(input('Quantidade de kg da Picanha: '))

    #Aqui define o preço 

    if contrafile <= 5 and alcatra <= 5 and picanha <= 5:
        preco_contrafile = contrafile * 4.9
        preco_alcatra = alcatra * 5.9
        preco_picanha = picanha * 6.9
    else:
        preco_contrafile = contrafile * 5.8
        preco_alcatra = alcatra * 6.8
        preco_picanha = picanha * 7.8

    #Compra ou não no cartão a loja

    lista = ["Sim", "Não"] #lista[0]=Sim, lista[1] = Não

    cartao_loja = str(input('Comprou no cartão da loja?'))

    if cartao_loja == lista[0]:
        valor_total = (preco_contrafile + preco_alcatra + preco_picanha) * 0.95
        print (valor_total)
    else:
        valor_total = (preco_contrafile + preco_alcatra + preco_picanha)
        print (valor_total)

if __name__ == "__main__":
    pagina_secundaria()
    opcao = input ('Escolha a opção:')

    if opcao == '1':
        frutas()
    
    if opcao == '2':
         carnes()
    