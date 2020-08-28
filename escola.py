
#MEDIA DE UMA TURMA EM UMA ESCOLA

idade_a = int (input('Digite a idade: '))
idade_b = int (input('Digite a idade: '))
idade_c = int (input('Digite a idade: '))
idade_d = int (input('Digite a idade: '))

y = [idade_a, idade_b, idade_c, idade_d]

x = sum(y)

#print(x)

media_idade = x / len(y) #len ==> comprimento da lista

print(media_idade)

if 0 <= media_idade <= 25 :
    print('Jovem')
elif 26 <= media_idade <= 60:
    print('Adulta')
elif media_idade > 60:
    print('Idosa')

"""
alunos = int(input('Quantidade de alunos:'))

i = 0

while i < alunos:
    nota = (input('Digite: '))
    i = i + 1
    x = list(nota)
    print(x)


#print(x)

media_idade = x / len(y) #len ==> comprimento da lista

print(media_idade)

if 0 <= media_idade <= 25 :
    print('Jovem')
elif 26 <= media_idade <= 60:
    print('Adulta')
elif media_idade > 60:
    print('Idosa'
"""