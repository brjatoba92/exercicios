"""
PROGRAMA CONTABILIDADE
- SALARIO LIQUIDO E BRUTO
- DESCONTOS : INSS, IR E SINDICATO
"""

#INSS

salario_bruto = float(input ('Digite seu salario: '))
ir = 0.11
inss = 0.08
sindicato = 0.05

descontos = salario_bruto * (ir + inss + sindicato) 

salario_liquido = salario_bruto - descontos

print ('Seu salario liquido:')
print (salario_liquido)

print ('Deduções: IR, INSS, SINDICATO')

imposto_renda = salario_bruto * ir
inss_2 = salario_bruto * inss
taxa_sindicato = salario_bruto * sindicato

deducoes = [imposto_renda, inss_2, taxa_sindicato]

print (deducoes)

