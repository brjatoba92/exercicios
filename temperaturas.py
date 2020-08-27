
#Conversao C para F/K
temperatura = float(input('Coloque a temperatura em Celsius: '))
taxa_ck = 273
taxa_cf = ((5/9) + 32)
    
#if __name__ == "__main__":

def conversao(*args):
    temp_kelvin = temperatura
    for n in args:
        temp_kelvin += n
    return temp_kelvin
    #return f'Kelvin {kel_fahr}: °C '

print(conversao (taxa_cf))
print(conversao(taxa_ck))

print ('Temperatura convertida!!')
"""
"""
#Conversao F/K para C
temperatura = float(input('Coloque a temperatura em Farenheit/Kelvin: '))

taxa_kc = (273)
taxa_fc = ((5/9))

    
#if __name__ == "__main__":

def conversao(*args):
    if temperatura >= 273:
        temp_cl = temperatura
        for n in args:
            temp_cl = temperatura - taxa_kc
        return temp_cl

    elif temperatura <273:
        temp_cl = temperatura
        for n in args:
            temp_cl = (temperatura -32) * taxa_fc 
        return temp_cl
        
if temperatura >= 273:
    print(conversao (taxa_kc))

else:
    print(conversao (taxa_fc))

print ('Temperatura convertida!!')

