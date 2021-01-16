# Bananas no arquivo
# Faça um programa que abre um arquivo texto chamado macacos-me-mordam.txt e imprime o número de ocorrências da palavra 'banana'. Atenção: palavras com letra maiúscula também devem ser contabilizadas, ou seja, se as palavras aparecerem assum: 'Banana', 'BANANA', 'BaNaNa', devem ser contadas como palavras. Exemplo de texto: 'Banana nanica banana da terra.'

with open("macacos-me-mordam.txt") as arquivo:
    conteudo = arquivo.read()
    normalized = conteudo.upper()
    length = len(normalized.split("BANANA")) - 1
    print(length)
