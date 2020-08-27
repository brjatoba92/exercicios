
#DENTRO/EXCEDENTE DA COTA

peso = float(input ('Digite a quantidade de quilos: '))
limite = 50 

if peso > limite:
    excedente = (peso - limite)
    multa = 4 * (peso - limite)
    #print (excedente)
else:
    pass

print ('Quilos excedente:')
print (excedente)
print ('Multa a ser paga:')
print (multa)
