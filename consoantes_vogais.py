
""" 
PROGRAMA VOGAL/ CONSOANTE
- Criar uma lista: vogal = ['a', 'e', 'i', 'o', 'u']
- vogal[0] ==> a ...

"""

letra = str(input('Digite uma letra:'))
vogal = ['a', 'e', 'i', 'o', 'u']

if letra in vogal:
    print ('Letra é uma vogal')
else:
    print ('Letra é uma consoante')