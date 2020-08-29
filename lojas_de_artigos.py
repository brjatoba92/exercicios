"""
PROGRAMA CAIXA SUPERMERCADO
"""

valor_unitario = 1.99
quantidade_compra = int(input('Informe a quantidade'))
conta = []
i = 1

for i in range(quantidade_compra):
    i += 1
    print("Produto", i, "=",i * valor_unitario)