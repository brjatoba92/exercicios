"""
PROGRAMA NUMEROS
PAR/IMPAR; POSITIVO/NEGATIVO, INTEIRO/DECIMAL

"""

numero_1 = float(input('Digite um numero: '))
numero_2 = float(input('Digite um numero: '))

def pagina_secundaria():
    print ('1. Par ou impar')
    print ('2. Positivo ou negativo')
    print ('3. Inteiro ou decimal')

def par_impar():

    if numero_1 % 2 == 0: #Se o resto da divisão for zero imprima par, se não imprima impar
        print ('Este numero é par')
    else:
        print('Este numero é impar')

    if numero_2 % 2 == 0: #Se o resto da divisão for zero imprima par, se não imprima impar
        print ('Este numero é par')
    else:
        print('Este numero é impar')

def pos_negativo():

    if numero_1 >=0:
        print ('Este numero é positivo')
    else:
        print('Este numero é negativo')

    if numero_2 >=0:
        print ('Este numero é positivo')
    else:
        print('Este numero é negativo')

def int_decimal():
    
    if int(numero_1) == numero_1:
        print('Este numero é inteiro')
    else:
        print('Este numero é decimal')
    if int(numero_2) == numero_2:
        print('Este numero é inteiro')
    else:
        print('Este numero é decimal')
    
if __name__ == "__main__":
    pagina_secundaria()
    opcao = input ('Escolha a opção:')

    if opcao == '1':
        par_impar()
    
    if opcao == '2':
        pos_negativo()
    
    if opcao == '3':
        int_decimal()