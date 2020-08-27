"""
PROGRAMA NOTAS
- INFORMA DUAS NOTAS
- QUANDO MAIOR QUE 7 E MENOR QUE 9 ==> APROVADO
- QUANDO MENOR QUE 7 ==> REPROVADO
- QUANDO IGUAL A 10 ==> APROVADO COM DESTAQUE
"""

# Aprovado / Reprovado

nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))

media = (nota_1 + nota_2)/2

if 7 <= media <= 9:
    print('Aprovado !!!')
elif media < 7:
    print('Reprovado !!!')
elif media == 10:
    print ('Aprovado com destaque !!!')
