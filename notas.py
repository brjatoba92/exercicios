"""
PROGRAMA MEDIA - CONCEITO, APROVADO/REPROVADO

"""
#Aprovado/Reprovado

nota_conceito1 = float(input('Digite sua nota: '))
nota_conceito2 = float(input('Digite sua nota: '))

media = (nota_conceito1 + nota_conceito2) / 2

if media > 9 and media <= 10:
    print ('Conceito: A')

elif media > 7.5 and media <= 9:
    print ('Conceito: B')

elif media > 6 and media <= 7.5:
    print ('Conceito: C')

elif media > 4 and media <= 6:
    print ('Conceito: D')

else:
    print ('Conceito: E')

print ('Resultado: ')

if media > 6:
    print ('Aprovado !!!')
else:
    print ('Reprovado !!!')