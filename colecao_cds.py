quantidade_cds = int(input('Informe a quantidade de cds:')) 
colecao = []
cd_inicial = 1

for i in range(quantidade_cds):
    print("CD", cd_inicial)
    cd_valor = colecao.append(float(input('Insira o valor do cd:')))
    cd_inicial += 1

media = sum(colecao) / len(colecao)
print("A media de valor da coleção é:", media, "Reais")