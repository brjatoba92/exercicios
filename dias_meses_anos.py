"""
PROGRAMA ANO BISSEXTO / DATA

- QUANTIDADE DE DIAS INFORMA SE É UM ANO BISSEXTO OU NÃO
- DIGITAR UMA DATA E INFORMAR SE É VALIDA OU NÃO

"""

def pagina_secundaria():
    
    print ('1. Ano Bissexto ')
    print ('2. Data ')


def bissexto():
    #Dias ano
    
    numero_anos = int(input ('Digite o numero de dias de um ano: '))

    if numero_anos == 366:
         print ('Este ano é bissexto')
    elif numero_anos == 365:
        print ('Este ano não é bissexto')

def data():

    dia = int (input ('Informe o dia'))
    mes = int (input ('Informe o mes'))
    ano = int (input ('Informe o ano'))

    #Data valida/invalida

    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia <= 30:
            valida = True

    elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia <= 31:
            valida = True

    elif mes == 2:
        if dia <= 28 or dia <= 29:
            valida = True


    if (valida):
        print ('Data valida')
    else:
        print ('Data invalida')


if __name__ == "__main__":
    pagina_secundaria()
    opcao = input ('Escolha a opção:')

    if opcao == '1':
        bissexto()
    
    if opcao == '2':
        data()
