colecao = []
compra_inicial = 1

while compra_inicial > 0:
    print("Compra", compra_inicial)
    compra = colecao.append(float(input('Insira o valor: ')))
    compra_inicial += 1
    
    x = str(input('Digite e para encerrar ou c para continuar: '))
    if x == "e":
        break
    elif x == "c":
        continue

valor_final = sum(colecao)
pagamento = int(input('Quanto o cliente pagou?'))
print("Total da compra: ", valor_final)
if valor_final < pagamento:
    troco = pagamento - valor_final
    print("Total da compra: ", valor_final, "Valor pago:", pagamento, "Troco", troco)

    

