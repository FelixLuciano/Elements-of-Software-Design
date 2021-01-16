# Teste de maioridade
# Escreva uma função que recebe a idade e verifica se a pessoa pode comprar bebida alcóolica no Brasil e/ou nos EUA, onde somente maiores de 21 anos podem comprar bebida alcóolica. Os possíveis resultados da função são: "Liberado EUA e BRASIL", "Liberado BRASIL" e "Não está liberado".
# O nome da sua função deve ser verifica_idade.

def verifica_idade (age):
    if age < 18:
        return "Não está liberado"
    elif age < 21:
        return "Liberado BRASIL"
    else:
        return "Liberado EUA e BRASIL"
