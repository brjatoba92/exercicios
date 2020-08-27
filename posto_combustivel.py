"""
PROGRAMA POSTO DE COMBUSTIVEL

- Criei um menu para o usuario digitar 1 (Alcool) e 2 (Gasolina)

- Define a quantidade de litros (alcool e gasolina)
- Define o valor dos combustiveis em função da quantidade de litros e o tipo
  - Acrescenta desconto
"""

litros = float(input('Quantidade de litros: '))

def pagina_inicial():
    print ('1. Alcool ')
    print ('2. Gasolina ')

#Alcool ==> 1,90/litro

def combustivel1():
    alcool = litros * 1.9
    if litros <= 20: #desconto de 3%/litro
        alcool_desconto = alcool * 0.97
        valor_alcool = alcool_desconto
    elif litros > 20: #desconto de 5%/litro
        alcool_desconto = alcool * 0.95
        valor_alcool = alcool_desconto
    print(valor_alcool)

def combustivel2():
    gasolina = litros * 2.5
    #Gasolina ==> 2,50/litro
    if litros <= 20: #desconto de 4%/litro
        gasolina_desconto = gasolina * 0.96
        valor_gasolina = gasolina_desconto
    elif litros > 20: #desconto de 6%/litro
        gasolina_desconto = gasolina * 0.94
        valor_gasolina = gasolina_desconto
    print(valor_gasolina)

if __name__ == "__main__":
    pagina_inicial()
    opcao = input ('Escolha a opção:')

    if opcao == '1':
        combustivel1()
    
    if opcao == '2':
        combustivel2()
