""" 
PROGRAMA FIBONACCI
By Bruno Jatoba
"""

"""
MENU
"""
def pagina_secundaria():
    
    print ('1. Enesimo valor a ser clicado')
    print ('2. Enesimo valor definido')

def enesimo():
    enesimo_valor = int(input('Digite o enesimo valor: '))
    x_j = 1 #ultimo elemento
    x_i = 1 #penultimo elemento

    i = 1
    print(x_j) #1
    print(x_i) #1


    while i <= enesimo_valor:
        proximo_elemento = x_j + x_i # 2 
        x_i = x_j #
        x_j = proximo_elemento
        i += 1
        print(proximo_elemento)

def fibonacci():

    x_j = 1 #ultimo elemento
    x_i = 1 #penultimo elemento

    i = 1
    print(x_j) #1
    print(x_i) #1

    while i <= 500:
        proximo_elemento = x_j + x_i # 2 
        x_i = x_j #
        x_j = proximo_elemento
        i += 1
        print(proximo_elemento)


if __name__ == "__main__":
    pagina_secundaria()
    opcao = input ('Escolha a opção:')

    if opcao == '1':
        enesimo()
    
    if opcao == '2':
        fibonacci()