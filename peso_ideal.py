
#PESO IDEAL

def pagina_inicial():
    print ('Programa para academia:')
    print ('1. Avaliação para homem')
    print ('2. AValiação para mulher')

def altura_homem():
    altura = float(input ('Digite sua altura: '))
    peso_ideal_homem = ((72.7 * altura) - 58)
    print ('Peso ideal para homem:')
    print (peso_ideal_homem)

def altura_mulher():
    altura = float(input ('Digite sua altura: '))
    peso_ideal_mulher =((62.1 * altura) - 44.7)
    print ('Peso ideal para homem:')
    print (peso_ideal_mulher)

if __name__ == "__main__":
    pagina_inicial()
    opcao = input ('Escolha a opção:')

    if opcao == '1':
        altura_homem()
    
    if opcao == '2':
        altura_mulher()

