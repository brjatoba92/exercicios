"""
PROGRAMA LISTA DE CARACTERES

- IMPRIME AS LETRAS E SUAS QUANTIDADES NA VERTICAL
"""

def contar_caracteres(s):
    """Função que conta os caracteres de um a string;

    param s: string a ser contada
    """

    ###contar_caracteres('bruno')
    ###contar_caracteres('banana')
    
    caracteres_ordenados = sorted (s)

    caracter_anterior = caracteres_ordenados[0]
    contagem = 1

    for caracter in caracteres_ordenados[1:]: #contar a partir do segundo elemento
        if caracter == caracter_anterior:
            contagem += 1
        else:
            print(f'{caracter_anterior}: {contagem}')
            caracter_anterior = caracter
            contagem = 1
    
    print(f'{caracter_anterior}: {contagem}')

if __name__ == "__main__":
    contar_caracteres('bruno jatoba')
    print()
    contar_caracteres('banana')
