quantidade_cds = int(input('Informe a quantidade de cds:')) 
cds = []
cd_inicial = 1

for i in range(quantidade_cds):
    print("CD", cd_inicial)
    cd_valor = cds.append(float(input('Insira o valor do cd:')))
    cd_inicial += 1

media = sum(cds) / len(cds)
print("A media de valor da coleção é: ", media, "Reais")