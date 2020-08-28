"""
PROGRAMA CONTAR CARACTERES DE UM NOME
"""

palavra = str(input('Digite uma palavra'))

def contar_caracteres(s):
    resultado = {}

    for caracter in s: #contar a partir do segundo elemento
      resultado [caracter] = resultado.get(caracter, 0) + 1
    
    return resultado    
    
if __name__ == "__main__":
    print(contar_caracteres(palavra))
    #print(contar_caracteres('banana'))