numero_1a25 = []
numero_26a50 = []
numero_51a75 = []
numero_76a100 = []

i = True

while i > 0:
    i = float(input('Digite um numero:'))
    if 0 < i <= 25:
        numero_1a25.append(i)
    if 25 < i <= 50:
        numero_26a50.append(i)
    if 50 < i <= 75:
        numero_51a75.append(i)
    if 75 < i <= 100:
        numero_76a100.append(i)
    
    x = str(input('Digite e para encerrar ou c para continuar: '))
    if x == "e":
        break
    elif x == "c":
        continue


print("[1,25]", len(numero_1a25))
print("[26,50]", len(numero_26a50))
print("[51,75]", len(numero_51a75))
print("[76,100]", len(numero_76a100))
    
    