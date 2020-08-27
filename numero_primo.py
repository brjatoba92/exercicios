"""
NUMERO PRIMO

- DIVISIVEL POR ELE MESMO E POR 1
- 1 E 2 NÃO SÃO PRIMOS
- 3,5,7,11,13,17,19,23,27,29,31,37,41,43,47,53,57,59,61,67,69,71,73,77,79,83,87,91,93,97,101,103,107,109
- QUANDO A SOMA DOS ALGARISMO É IGUAL A 3 NÃO É PRIMO

"""
numero_primoounao = int(input("Digite um numero: "))
divisão_por1 = 0

""" AQUI DEFINE OS VALORES PRIMOS """
if numero_primoounao >= 3: #aceitar somente valores maiores o igual a 3, pois 1 e 2 não são primos
    for divisão_por_elemesmo in range(1, numero_primoounao): #para um valor estiver na lista variando de 1 até o valor definido 
        if numero_primoounao % divisão_por_elemesmo == 0: #aqui aponta se o numero é dividido por ele mesmo (resto igual a zero)
            divisão_por1 = divisão_por1 + 1 #divisão por 1 ==> 0 + 1 = 1
            if divisão_por1 > 1:  #aqui limita a divisão somente por 1
              break
    if divisão_por1 > 1:
      print("Este numero não é primo !!!")
    else:
      print(numero_primoounao)
      print("Este numero é primo !!!!")
else: #aqui aponta valores menores que 3 (0 a 2) 
    print("Este numero não é primo !!!")



