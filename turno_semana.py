
#Turno

letra = str(input('Digite a letra:'))
lista = {'M':'matutino', 'V':'vespertino', 'N':'noturno'}

if letra in lista:
    print('Bom dia!!!!')
elif letra in lista:
    print('Boa tarde!!!!')
elif letra in lista:
    print('Boa noite!!!!')
else:
    print('Nome invalido!!!')




# Dia semana
dia_semana = str (input ('Digite o dia da semana: '))

lista_semana = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado']


if dia_semana in lista_semana:
    print (dia_semana)

else:
    print ('Dia invalido !!!')

