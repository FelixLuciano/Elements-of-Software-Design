# Quantos dias se passaram?
# Faça uma função que recebe uma data, representada por uma string, e devolve a quantidade de dias que já se passaram desde o início daquele ano. As datas sempre serão representadas por uma string contendo dois dígitos para o dia, dois dígitos para o mês e 4 dígitos para o ano. Você pode assumir que não serão considerados anos bissextos, ou seja, fevereiro sempre possui 28 dias (consequentemente o ano sempre terá 365 dias).
# Exemplos:
# - Para a entrada '01/01/2018', sua função deve retornar 0, pois ainda não se passou nenhum dia desde o início de 2018 no dia primeiro de janeiro.
# - Para a entrada '15/03/2019', sua função deve retornar 73, pois já se passaram 31+28+14=73 dias (janeiro e fevereiro inteiros mais 14 dias).
# - Para a entrada '31/12/2021', sua função deve retornar 364, pois é o último dia do ano.
# O nome da sua função deve ser 'dias_do_ano'.

def dias_do_ano (date):
    # Extrai dia, mês e ano, respectivamente, da string em formado DD/MM/AAAA
    day, mounth, year = [int(date_info) for date_info in date.split("/")]
    
    # Número de dias com base no dia do mês
    days_in_day = day - 1
    
    # Numero de dias com base no mês do ano
    days_in_mounth = 0

    # Conta a quantidade de dias no mêses inteiros até o mês atual
    for month_i in range(1, mounth):
        # Conta mêses de 31 dias
        if month_i in (1, 3, 5, 7, 8, 10, 12):
            days_in_mounth += 31
        # Conta mêses de 30 dias
        elif month_i in (4, 6, 9, 11):
            days_in_mounth += 30
        # Conta fevereiro com 28 dias
        else:
            days_in_mounth += 28
    
    # Determina os dias no ano com base nos dias no dia atual e nos mêses
    days_in_year = days_in_day + days_in_mounth
    
    return days_in_year

# Feedback do professor:
# "excelente, muito bom"
