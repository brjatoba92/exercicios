#Desconto

salario_bruto = float(input('Digite o salario:'))

sindicato = 0.03
fgts =  0.11
inss = 0.1

valor_sindicato = salario_bruto
valor_fgts = salario_bruto * fgts
valor_inss = salario_bruto * inss
#descontos_primarios = valor_fgts + valor_inss + valor_sindicato

"""
IR = 900 ==> ISENTO
    1500 ==> -5%
    2500 ==> -10%
    ACIMA DE 2500 ==> -20%
"""

if salario_bruto <= 900:
    #ir = salario_bruto * 0.05
    descontos = valor_inss
    salario_liquido = salario_bruto - (descontos)
elif salario_bruto > 900 and salario_bruto <= 1500:
    ir = 0.05
    valor_ir = salario_bruto * ir
    descontos = valor_inss + valor_ir
    salario_liquido = salario_bruto - descontos
elif salario_bruto > 1500 and salario_bruto <= 2500:
    ir = 0.1
    valor_ir = salario_bruto * ir
    descontos = valor_fgts + valor_inss + valor_sindicato + valor_ir
    salario_liquido = salario_bruto - descontos
else:
    ir = 0.20
    valor_ir = salario_bruto * ir
    descontos = valor_inss + valor_ir
    salario_liquido = salario_bruto - descontos

print('Salario bruto: ')
print(salario_bruto)

if salario_bruto <= 900:
    pass
else:
    print('Imposto de Renda: ')
    print(valor_ir)

print('FGTS: ')
print(valor_fgts)

print('INSS')
print(valor_inss)

print('Descontos: ')
print(descontos)

print('Salario Liquido: ')
print(salario_liquido)

print('Custo do empregador:')
custo_empregador = salario_bruto + valor_fgts
print(custo_empregador)
