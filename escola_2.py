
#MEDIA DE UMA TURMA EM UMA ESCOLA

quantidade_turmas = int(input('Digite a quantidade de turmas:'))
alunos_porturma = []

i = 1

for i in range(quantidade_turmas):
    print("Quantidade de turmas,", i)
    alunos = int (input('Digite a quantidade de alunos: '))
    while alunos > 40:
        print("Esta turma sóm tem", i)
        alunos = int(input('Aluno turma: '))
    i += 1
    alunos_porturma.append(alunos) #função append inclui valores dentro de uma lista/tupla

media = sum(alunos_porturma) / len(alunos_porturma)

print("A media da quantidade de alunos por turma é:", media)

"""
while i < quantidade_turmas:
    i += 1
    alunos = int (input('Digite a quantidade de alunos: '))
    print(alunos)
"""