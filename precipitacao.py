precipitacao_hoje = float(input('Informe a precipitação horaria: '))


def teste (variavel_meteorologica):
    if precipitacao_hoje > 60:
        return f'Precipitação forte ({variavel_meteorologica} mm/h) : ALERTA!!!! CONTATE URGENTE A DEFESA CIVIL 999'
    elif 5.1 <= precipitacao_hoje <60:
        return f'Precipitação moderada ({variavel_meteorologica} mm/h) : REQUER MONITORAMENTO'
    elif 1.1 <= precipitacao_hoje <5.1:
        return f'Precipitação fraca ({variavel_meteorologica} mm/h) : TEMPO NORMAL'
    else:
        return f'Precipitacao insignificante'

retorno = teste (precipitacao_hoje)
print (retorno)

