"""
PROGRAMA INVESTIGAÇÃO CRIME - CSI

- Faz 5 perguntas
- Com base na resposta atribui 4 classificações
  Inocente = com respostas positivas inferior a 2
  Suspeito = igual a 2 positivas
  Cumplice = 3 ou 4 positivas
  Acusado = as 5 positivas

- Define como inteiro para capiturar o valor da resposta na pergunta: 1(Sim), 0 (Não)
- Somar os valores
"""
def respostas():

    print ('1. Ligou para a vitima? ')
    resposta_investigado1 = int(input ('Informe 1/Sim ou 0/Não:'))

    print ('2. Esteve no local do crime? ')
    resposta_investigado2 = int(input ('Informe 1/Sim ou 0/Não:'))

    print ('3. Mora perto da vítima? ')
    resposta_investigado3 = int(input ('Informe 1/Sim ou 01/Não:'))

    print ('4. Devia para a vítima? ')
    resposta_investigado4 = int(input ('Informe 1/Sim ou 0/Não:'))

    print ('5. Já trabalhou com a vítima? ')
    resposta_investigado5 = int(input ('Informe 1/Sim ou 0/Não:'))

    soma_resposta = resposta_investigado1 + resposta_investigado2 + resposta_investigado3 + resposta_investigado4 + resposta_investigado5
    
    if soma_resposta == 5:
        print('Acusado')
    elif 3 <= soma_resposta < 5:
        print('Cumplice')
    elif soma_resposta == 2:
        print('Suspeito')
    else:
        print('Inocente')
        

    
if __name__ == "__main__":
    respostas()

    