# Aniversariantes de setembro
# Faça uma função que recebe um dicionário cujas chaves são nomes de pessoas e os valores são as respectivas datas de nascimento no formato 'dd/mm/aaaa', onde dd são dois caracteres representando o dia, mm são dois caracteres representando o mês e aaaa são quatro caracteres representando o ano. A função deve devolver um novo dicionário contendo somente os dados (nome e data de nascimento) dos aniversariantes de setembro.
# O nome da sua função deve ser 'aniversariantes_de_setembro'.

def aniversariantes_de_setembro (birthdays):
    sep_birthdays = {}

    for name, birthday in birthdays.items():
        day, month, year = birthday.split("/")

        if month == "09":
            sep_birthdays[name] = birthday

    return sep_birthdays
