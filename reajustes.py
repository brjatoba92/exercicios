#Reajustes

salario = float(input('Digite a letra:'))

if salario <= 280:
    reajuste = salario * 0.20
    percentual = '20%'
    novo_salario = salario * 1.20
elif salario > 280 and salario <= 700:
    reajuste = salario * 0.15
    percentual = '15%'
    novo_salario = salario * 1.20
elif salario > 700 and salario <= 1500:
    reajuste = salario * 0.10
    percentual = '10%'
    novo_salario = salario * 1.20
else:
    reajuste = salario * 0.05
    percentual = '5%'
    novo_salario = salario * 1.20

print('Salario: ')
print (salario)
print('Reajuste: ')
print (reajuste)
print('Percentua aplicado: ')
print (percentual)
#print (salario + reajuste)
print('Novo salario: ')
print (novo_salario)
