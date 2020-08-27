#Produto mais barato

produto_1 = float(input('Digite o preço do primeiro produto: '))
produto_2 = float(input('Digite o preço do segundo produto: '))
produto_3 = float(input('Digite o preço do terceiro produto: '))

lista = [produto_1, produto_2, produto_3]

if min(lista) == lista[0]:
    print('Mais barato é o primeiro')
    print (max (lista))
elif min(lista) == lista[1]:
    print('Mais barato o segundo')
    print (max (lista))
elif min(lista) == lista[2]:
    print('Mais barato o terceiro')
    print (max (lista))
