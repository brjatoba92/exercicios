""" MENU DE OPÇÕES """

def pagina_secundaria():
    print ('1. Triangulo')
    print ('2. Equação do Segundo Grau')


"""
MODULO TRIANGULO

Equilatero: tres lados iguais
Isosceles: dois lados iguais
Retangulo : tres lados diferentes

and: os termos tem que ser ambos verdadeiros
or: um dos termos tem que ser verdadeiro

"""

def triangulo():
    lado_1 = float (input ('Digite o primeiro lado: '))
    lado_2 = float (input ('Digite o segundo lado: '))
    lado_3 = float (input ('Digite o terceiro lado: '))

    if (lado_1 == lado_2) and (lado_1 == lado_3):
        print ('Este triangulo é equilatero')

    elif (lado_1 == lado_2) or (lado_1 == lado_3) or (lado_2 == lado_3):
        print ('Este triangulo é isosceles')

    else:
        print('Este triangulo é retangulo')


"""
MODULO EQUACAO DO SEGUNDO GRAU

Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

"""
def equacao_2grau():
    print('Calculando as raízes de uma equação de 2º grau\n')
    a = float(input('Entre com o valor de a: '))
    b = float(input('Entre com o valor de b: '))
    c = float(input('Entre com o valor de c: '))

    delta = (b ** 2 - 4 * a *c)

    if a == 0:
        pass
    elif delta < 0:
        pass
    else:
        x_1 = (-b + (delta ** (1/2))) / (2 * a)
        x_2 = (-b - (delta ** (1/2))) / (2 * a) 
        print (x_1, x_2)

    if a == 0:
        print ('Esta equação não é do segundo grau. Programa encerrado')

    elif delta < 0:
        print ('Delta negativo. Programa encerrado')

    else:
        print ('Calculado com sucesso!!!')   


if __name__ == "__main__":
    pagina_secundaria()
    opcao = input ('Escolha a opção:')

    if opcao == '1':
        triangulo()
    
    if opcao == '2':
         equacao_2grau()

