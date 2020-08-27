"""
CARTÃO DE CREDITO 
- MOSTRA SE UMA FATURA FOI PAGA EM DIA OU NÃO
- SE FATURA PAGA ATÉ O DIA ==> ESTA EM DIA
- CASO PASSE DO DIA ==> ATRASADA E MOSTRA UMA MENSAGEM PARA REGULARIZAR O DEBITO
"""
valor_original = float(input('Informe o valor: '))
taxa = 0.05
juros_diarios = 0.002
dia_pagamento = int(input('Informe o dia do seu pagamento: '))
dia_vencimento = 25
dias_de_atraso = dia_pagamento - dia_vencimento

cliente = {'nome': 'Bruno', 'sobrenome': 'Jatobá'}

def adimplente_inadiplente (**cliente):
    print (**cliente)
print (cliente)

def fatura_emdia_vencida(*args):
    if dia_pagamento > dia_vencimento:   
        ac = valor_original
        for n in args:
            ac += n
        return ac
    elif dia_pagamento <= dia_vencimento:
        ac = valor_original
        for n in args:
            ac = n
        return ac

if dia_pagamento > dia_vencimento:
    print(fatura_emdia_vencida(valor_original * taxa, valor_original * juros_diarios * dias_de_atraso))
    print ('Evite o bloqueio do seu cartão. Entre em contato conosco: 0800 789 8874')
elif dia_pagamento <= dia_vencimento:
    print(valor_original)
    print('Parabens!!! Voce esta em dia')

if __name__ == "__main__":
    fatura_emdia_vencida()