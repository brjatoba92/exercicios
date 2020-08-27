"""
PROGRAMA CADASTRO USUARIO

- Nome superior a 3 caracteres ===> usando a função len() e restringir a quantidade de caracteres igual o maior que 3
- Informar o salario (maior que zero)
- Sexo do usuario
- Estado civil

"""


nome = str(input('Digite seu nome completo'))
#x = nome[0]
#print(x)
idade = int(input('Digite sua idade: '))

salario = int(input('Digite seu salario'))

sexo = str(input('Digite seu sexo. f/Feminino, m/Masculino: '))

sexo_siglas = ['f', 'm'] #siglas do sexo

estado_civil = str(input('Digite seu estado civil. s/Solteiro(a), c/Casado(a), v/Viuvo(a), d/Divorciado(a): '))

civil_siglas = ['s', 'c', 'v', 'd'] #siglas do estado civil



if len(nome) >= 3: #se o tamanho do nome for igual ou superior a zero imprima o nome
    print(nome)
else:
    pass

if  0 < idade < 150:
    print('Idade valida')
else:
    pass

if salario > 0:
    print (salario)
else:
    pass

if sexo == sexo_siglas[0]:
    print('Fenimino')
elif sexo == sexo_siglas[1]:
    print('Masculino')
else:
    pass

if estado_civil == civil_siglas[0]:
    print('Solteiro(a)')
elif estado_civil == civil_siglas[1]:
    print('Casado(a)')
elif estado_civil == civil_siglas[2]:
    print('Viuvo(a)')
elif estado_civil == civil_siglas[3]:
    print('Divorciado(a)')
else:
    pass
