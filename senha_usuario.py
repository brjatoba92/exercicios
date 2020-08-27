usuario = str(input("Informe o nome de usuario"))
senha = str(input("Informe sua senha:"))

while senha == usuario:
    print('Senha invalida. Digite novamente')
    usuario = str(input("Informe o nome de usuario"))
    senha = str(input("Informe sua senha:"))
else:
    print('Casdastro efeutuado com sucesso!!!')