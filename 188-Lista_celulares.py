# Lista celulares
# O departamento de marketing da sua empresa está interessado em obter apenas os números de telefone celular, separando-os dos telefones fixos. Para simplificar esta operação serão considerados números de celular apenas aqueles que, após o código de área, iniciarem com o dígito adicional 9.
# Você recebeu a tarefa de obter uma lista com os números de celular, sem o código de área. Entretanto, o cadastro de telefones do departamento de marketing não está padronizado e existem números seguindo 3 formatos distintos:
# 1. Números completos (13 ou 14 caracteres), incluindo o código do país (+55) e o código de área (ex: 11). Exemplos: '+5511912345678' ou '+551133334444' (note que ambos começam com o caractere '+');
# 2. Número contendo apenas o código de área (10 ou 11 caracteres). Exemplos: '11987654321' ou '1155556666';
# 3. Número sem código de área (8 ou 9 caracteres). Exemplos: '918273645' ou '77778888'.
# Note que em todos os casos, o primeiro exemplo é um número de celular e o segundo não.
# Faça uma função que recebe uma lista de números de telefone e devolve uma lista contendo apenas os telefones celulares. Cada telefone da lista de entrada (recebida como argumento da sua função) pode estar em qualquer um dos 3 formatos acima. Os telefones da lista de saída (retornada pela sua função) devem conter apenas os dígitos do telefone, removendo o código do país e código de área se for necessário.
# Exemplo: a chamada lista_celulares(['+5511912345678', '1155556666', '77778888', '+551133334444', '918273645', '11987654321']) deve retornar a lista ['912345678', '918273645', '987654321']
# O nome da sua função deve ser lista_celulares.
