"""
PROGRAMA URNA ELETRONICA
- DEFINE NUMERO DE ELEITORES
- MOSTRA VOTOS POR CANDIDATO
"""

eleitores = int(input('Quantidade de eleitores:'))
candidato_a = 0
candidato_b = 0
candidato_c = 0

i = 0

while i < eleitores:
    voto = int(input('Seu voto: Digite 1 para A, 2 para B e 3 para C: '))
    if (voto == 1):
        candidato_a = candidato_a + 1
    elif (voto == 2):
        candidato_b = candidato_b + 1
    elif (voto == 3):
        candidato_c = candidato_c + 1
    i = i + 1

print("Candidato A:", candidato_a, "votos")
print("Candidato B:", candidato_b, "votos")
print("Candidato C:", candidato_c, "votos")
