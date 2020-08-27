"""
PROGRAMA CAIXA BANCO

- INFORMAR O VALOR A SER SACADO
-  OPÇÃO DAS NOTAS
- DISTRIBUI AS CEDULAS DISPONIVEIS CONFORME A OPÇÃO ESCOLHIDA 
"""
saque = int (input ('Digite o valor:'))

if 10 <= saque <= 600: #LIMITE DO CAIXA
    print ('Valor informado:')
    print (saque)
else:
    print ('Valor indisponivel nesse caixa')

print ('Notas disponiveis')

cedulas = (100, 50, 10, 5, 1) #CEDULAS DISPONIVEIS 

"""
MENU
"""
def pagina_secundaria():
    
    if (saque % cedulas[0]) == 0: #VALOR SACADO DIVIDIDO POR 100, DISPONEIS TODAS AS NOTAS
        print ('1. Notas de 100')
        print ('2. Notas de 50')
        print ('3. Notas de 10')
        print ('4. Notas de 5')
        print ('5. Notas de 1')
        print ('6. Notas de 100, 50, 10, 5 e 1')
        print ('7. Notas de 100, 50, 10, 5')
        print ('8. Notas de 100, 50, 10, 1')
        print ('9. Notas de 100, 50, 10')
        print ('10. Notas de 100, 50, 5')
        print ('11. Notas de 100, 50, 1')
        print ('12. Notas de 100 e 50')
        print ('13. Notas de 100 e 10')
        print ('14. Notas de 100 e 5')
        print ('15. Notas de 100 e 1')
        print ('16. Notas de 50 e 10')
        print ('17. Notas de 50 e 5')
        print ('18. Notas de 50 e 1')
        print ('19. Notas de 10 e 5')
        print ('20. Notas de 10 e 1')
        print ('21. Notas de 5 e 1')
        
    elif cedulas[1] < saque < cedulas[0]: #ENTRE 55 E 90
        print ('13. Notas de 50 e 10')
        print ('14. Notas de 50 e 5')
        print ('15. Notas de 50 e 1')
        print ('16. Notas de 10 e 5')
        print ('17. Notas de 5 e 1')
    
    elif saque < cedulas[2]: #ENTRE 10 e 49
         print ('16. Notas de 10 e 5')
         print ('17. Notas de 5 e 1')
    
    elif 100 < saque < 150 and (saque % cedulas[0]) > 0: #ENTRE 100 E 150 E O VALOR DO RESTO FOR MAIOR QUE 0 ==> 110 = SOBRA 10, 120 = SOBRA 20
        print ('13. Notas de 100 e 10')
        print ('14. Notas de 100 e 10')
        print ('15. Notas de 100 e 1')
        print ('16. Notas de 50 e 10')
        print ('17. Notas de 50 e 5')
        print ('18. Notas de 50 e 1')
        print ('19. Notas de 10 e 5')
        print ('20. Notas de 5 e 1')
    
    elif 200 < saque <= 250 and (saque % cedulas[0]) > 0: #ok
        print ('13. Notas de 100 e 10')
        print ('14. Notas de 100 e 5')
        print ('15. Notas de 100 e 1')
        print ('16. Notas de 50 e 10')
        print ('17. Notas de 50 e 5')
        print ('18. Notas de 50 e 1')
        print ('19. Notas de 10 e 5')
        print ('20. Notas de 5 e 1')

    elif 300 < saque <= 350 and (saque % cedulas[0]) > 0: #ok
        print ('13. Notas de 100 e 10')
        print ('14. Notas de 100 e 5')
        print ('15. Notas de 100 e 1')
        print ('16. Notas de 50 e 10')
        print ('17. Notas de 50 e 5')
        print ('18. Notas de 50 e 1')
        print ('19. Notas de 10 e 5')
        print ('20. Notas de 5 e 1')

    elif 400 < saque <= 450 and (saque % cedulas[0]) > 0: #ok
        print ('13. Notas de 100 e 10')
        print ('14. Notas de 100 e 5')
        print ('15. Notas de 100 e 1')
        print ('16. Notas de 50 e 10')
        print ('17. Notas de 50 e 5')
        print ('18. Notas de 50 e 1')
        print ('19. Notas de 10 e 5')
        print ('20. Notas de 5 e 1')

    elif 500 < saque <= 550 and (saque % cedulas[0]) > 0: #ok
        print ('13. Notas de 100 e 10')
        print ('14. Notas de 100 e 5')
        print ('15. Notas de 100 e 1')
        print ('16. Notas de 50 e 10')
        print ('17. Notas de 50 e 5')
        print ('18. Notas de 50 e 1')
        print ('19. Notas de 10 e 5')
        print ('20. Notas de 5 e 1')
    else:
        print ('6. Notas de 100, 50, 10, 5 e 1')
        print ('7. Notas de 100, 50, 10, 5')
        print ('8. Notas de 100, 50, 10, 1')
        print ('9. Notas de 100, 50, 10')
        print ('10. Notas de 100, 50, 5')
        print ('11. Notas de 100, 50, 1')
        print ('13. Notas de 100 e 10')
        print ('14. Notas de 100 e 5')
        print ('15. Notas de 100 e 1')
        print ('16. Notas de 50 e 10')
        print ('17. Notas de 50 e 5')
        print ('18. Notas de 50 e 1')
        print ('19. Notas de 10 e 5')
        print ('20. Notas de 5 e 1')

"""
OPÇÕES
"""

def opcao_1(): #ok
    quantidade_notas = divmod(saque, cedulas[0])
    print(quantidade_notas[0])
    
def opcao_2(): #ok
    quantidade_notas = divmod(saque, cedulas[1])
    print(quantidade_notas[0])

def opcao_3(): #ok
    quantidade_notas = divmod(saque, cedulas[2])
    print(quantidade_notas[0])

def opcao_4(): #ok
    quantidade_notas = divmod(saque, cedulas[2])
    print(quantidade_notas[0])

def opcao_5(): #ok
    quantidade_notas = divmod(saque, cedulas[2])
    print(quantidade_notas[0])

def opcao_6(): #ok
    quantidade_notas = divmod(saque, cedulas[0]) # 1 nota de 100
    x_100 = quantidade_notas[0] #1 nota de 100
    y_100 = quantidade_notas[1] #sobrou
    print(x_100,y_100)
    
    notas_a = divmod(y_100, cedulas[1])
    x_50 = notas_a[0] #1 nota de 50
    y_50 = notas_a[1] #sobrou
    print(x_50,y_50)
    
    notas_a = divmod(y_50, cedulas[2])
    x_10 = notas_a[0] #1 nota de 10
    y_10 = notas_a[1] #sobrou
    print(x_10,y_10)

    notas_a = divmod(y_10, cedulas[3])
    x_5 = notas_a[0] #1 nota de 5
    y_5 = notas_a[1] #sobrou
    print(x_5,y_5)

    notas_a = divmod(y_5, cedulas[4])
    x_1 = notas_a[0] #1 nota de 1
    y_1 = notas_a[1] #sobrou
    print(x_1, y_1)

    soma = x_100 + x_50 + x_10 + x_5 + x_1
    print(soma)

def opcao_7(): #ok
    quantidade_notas = divmod(saque, cedulas[0]) # 1 nota de 100
    x_100 = quantidade_notas[0] #1 nota de 100
    y_100 = quantidade_notas[1] #sobrou
    print(x_100,y_100)
    
    notas_a = divmod(y_100, cedulas[1])
    x_50 = notas_a[0] #1 nota de 50
    y_50 = notas_a[1] #sobrou
    print(x_50,y_50)
    
    notas_a = divmod(y_50, cedulas[2])
    x_10 = notas_a[0] #1 nota de 10
    y_10 = notas_a[1] #sobrou
    print(x_10,y_10)

    notas_a = divmod(y_10, cedulas[3])
    x_5 = notas_a[0] #1 nota de 5
    y_5 = notas_a[1] #sobrou
    print(x_5,y_5)

    soma = x_100 + x_50 + x_10 + x_5
    print(soma)

def opcao_8(): #ok
    quantidade_notas = divmod(saque, cedulas[0]) # 1 nota de 100
    x_100 = quantidade_notas[0] #1 nota de 100
    y_100 = quantidade_notas[1] #sobrou
    print(x_100,y_100)
    
    notas_a = divmod(y_100, cedulas[1])
    x_50 = notas_a[0] #1 nota de 50
    y_50 = notas_a[1] #sobrou
    print(x_50,y_50)
    
    notas_a = divmod(y_50, cedulas[2])
    x_10 = notas_a[0] #1 nota de 10
    y_10 = notas_a[1] #sobrou
    print(x_10,y_10)

    notas_a = divmod(y_5, cedulas[4])
    x_1 = notas_a[0] #1 nota de 1
    y_1 = notas_a[1] #sobrou
    print(x_1, y_1)

    soma = x_100 + x_50 + x_10 + x_1
    print(soma)

def opcao_9(): #ok
    quantidade_notas = divmod(saque, cedulas[0]) # 1 nota de 100
    x_100 = quantidade_notas[0] #1 nota de 100
    y_100 = quantidade_notas[1] #sobrou
    print(x_100,y_100)
    
    notas_a = divmod(y_100, cedulas[1])
    x_50 = notas_a[0] #1 nota de 50
    y_50 = notas_a[1] #sobrou
    print(x_50,y_50)
    
    notas_a = divmod(y_50, cedulas[2])
    x_10 = notas_a[0] #1 nota de 10
    y_10 = notas_a[1] #sobrou
    print(x_10,y_10)

    soma = x_100 + x_50 + x_10
    print(soma)

def opcao_10(): #ok
    quantidade_notas = divmod(saque, cedulas[0]) # 1 nota de 100
    x_100 = quantidade_notas[0] #1 nota de 100
    y_100 = quantidade_notas[1] #sobrou
    print(x_100,y_100)
    
    notas_a = divmod(y_100, cedulas[1])
    x_50 = notas_a[0] #1 nota de 50
    y_50 = notas_a[1] #sobrou
    print(x_50,y_50)
    
    notas_a = divmod(y_50, cedulas[3])
    x_5 = notas_a[0] #1 nota de 5
    y_5 = notas_a[1] #sobrou
    print(x_5,y_5)

    soma = x_100 + x_50 + x_5
    print(soma)

def opcao_11(): #ok
    quantidade_notas = divmod(saque, cedulas[0]) # 1 nota de 100
    x_100 = quantidade_notas[0] #1 nota de 100
    y_100 = quantidade_notas[1] #sobrou
    print(x_100,y_100)
    
    notas_a = divmod(y_100, cedulas[1])
    x_50 = notas_a[0] #1 nota de 50
    y_50 = notas_a[1] #sobrou
    print(x_50,y_50)
    
    notas_a = divmod(y_5, cedulas[4])
    x_1 = notas_a[0] #1 nota de 1
    y_1 = notas_a[1] #sobrou
    print(x_1, y_1)

    soma = x_100 + x_50 + x_1
    print(soma)

def opcao_12(): #ok
    quantidade_notas = divmod(saque, cedulas[0]) # 1 nota de 100
    x_100 = quantidade_notas[0] #1 nota de 100
    y_100 = quantidade_notas[1] #sobrou
    print(x_100,y_100)
    
    notas_a = divmod(y_100, cedulas[1])
    x_50 = notas_a[0] #1 nota de 50
    y_50 = notas_a[1] #sobrou
    print(x_50,y_50)
    
    soma = x_100 + x_50
    print(soma)

def opcao_13(): #ok
    quantidade_notas = divmod(saque, cedulas[0]) # 1 nota de 100
    x_100 = quantidade_notas[0] #1 nota de 100
    y_100 = quantidade_notas[1] #sobrou
    print(x_100,y_100)
    
    notas_a = divmod(y_100, cedulas[2])
    x_10 = notas_a[0] #1 nota de 10
    y_10 = notas_a[1] #sobrou
    print(x_10,y_10)
    
    soma = x_100 + x_10
    print(soma)

def opcao_14(): #ok
    quantidade_notas = divmod(saque, cedulas[0]) # 1 nota de 100
    x_100 = quantidade_notas[0] #1 nota de 100
    y_100 = quantidade_notas[1] #sobrou
    print(x_100,y_100)
    
    notas_a = divmod(y_100, cedulas[3])
    x_5 = notas_a[0] #1 nota de 5
    y_5 = notas_a[1] #sobrou
    print(x_5,y_5)
    
    soma = x_100 + x_5
    print(soma)

def opcao_15(): #ok
    quantidade_notas = divmod(saque, cedulas[0]) # 1 nota de 100
    x_100 = quantidade_notas[0] #1 nota de 100
    y_100 = quantidade_notas[1] #sobrou
    print(x_100,y_100)
    
    notas_a = divmod(y_100, cedulas[4])
    x_1 = notas_a[0] #1 nota de 1
    y_1 = notas_a[1] #sobrou
    print(x_1, y_1)
    
    soma = x_100 + x_1
    print(soma)

def opcao_16(): #ok
    notas_a = divmod(y_100, cedulas[1])
    x_50 = notas_a[0] #1 nota de 50
    y_50 = notas_a[1] #sobrou
    print(x_50,y_50)
    
    notas_a = divmod(y_50, cedulas[4])
    x_10 = notas_a[0] #1 nota de 1
    y_10 = notas_a[1] #sobrou
    print(x_10, y_10)
    
    soma = x_50 + x_10
    print(soma)

def opcao_17(): #ok 100(0), 50 (1), 10(2), 5(3), 1(4) 
    notas_a = divmod(saque, cedulas[1])
    x_50 = notas_a[0] #1 nota de 50
    y_50 = notas_a[1] #sobrou
    print(x_50,y_50)
    
    notas_a = divmod(y_50, cedulas[3])
    x_5 = notas_a[0] #1 nota de 5
    y_5 = notas_a[1] #sobrou
    print(x_5, y_5)
    
    soma = x_50 + x_5
    print(soma)

def opcao_18(): #ok 100(0), 50 (1), 10(2), 5(3), 1(4) 
    notas_a = divmod(saque, cedulas[1])
    x_50 = notas_a[0] #1 nota de 50
    y_50 = notas_a[1] #sobrou
    print(x_50,y_50)
    
    notas_a = divmod(y_50, cedulas[4])
    x_1 = notas_a[0] #1 nota de 5
    y_1 = notas_a[1] #sobrou
    print(x_1, y_1)
    
    soma = x_50 + x_1
    print(soma)

def opcao_19(): #ok 100(0), 50 (1), 10(2), 5(3), 1(4) 
    notas_a = divmod(saque, cedulas[2])
    x_10 = notas_a[0] #1 nota de 50
    y_10 = notas_a[1] #sobrou
    print(x_10,y_10)
    
    notas_a = divmod(y_50, cedulas[3])
    x_5 = notas_a[0] #1 nota de 5
    y_5 = notas_a[1] #sobrou
    print(x_5, y_5)
    
    soma = x_10 + x_5
    print(soma)

def opcao_20(): #notas de 10 e 1
    notas_a = divmod(saque, cedulas[2])
    x_10 = notas_a[0] #1 nota de 50
    y_10 = notas_a[1] #sobrou
    print(x_10,y_10)
    
    notas_b = divmod(y_10, cedulas[4])
    x_1 = notas_b[0] #1 nota de 5
    y_1 = notas_b[1] #sobrou
    print(x_1, y_1)
    
    soma = x_10 + x_1
    print(soma)

def opcao_21(): #notas de 5 e 1
    notas_a = divmod(saque, cedulas[3])
    x_5 = notas_a[0] #1 nota de 50
    y_5 = notas_a[1] #sobrou
    print(x_5,y_5)
    
    notas_b = divmod(y_5, cedulas[4])
    x_1 = notas_b[0] #1 nota de 5
    y_1 = notas_b[1] #sobrou
    print(x_1, y_1)

    soma = x_5 + x_1
    print(soma)

"""
APONTA PARA AS OPÇÕES

"""
if __name__ == "__main__":
    pagina_secundaria()
    opcao = input ('Escolha a opção:')

    if opcao == '1':
        opcao_1()
    
    if opcao == '2':
        opcao_2()
    
    if opcao == '3':
        opcao_3()
    
    if opcao == '4':
        opcao_4()
    
    if opcao == '5':
        opcao_5()

    if opcao == '6':
        opcao_6()
    
    if opcao == '7':
        opcao_7()
    
    if opcao == '8':
        opcao_8()
    
    if opcao == '9':
        opcao_9()
    
    if opcao == '10':
        opcao_10()
    
    if opcao == '11':
        opcao_11()
    
    if opcao == '12':
        opcao_12()

    if opcao == '13':
        opcao_13()
    
    if opcao == '14':
        opcao_14()
        
    if opcao == '15':
        opcao_15()

    if opcao == '16':
        opcao_16()
    
    if opcao == '17':
        opcao_17()
    
    if opcao == '18':
        opcao_18()
    
    if opcao == '19':
        opcao_19()
    
    if opcao == '20':
        opcao_20()
    
    if opcao == '20':
        opcao_20()
