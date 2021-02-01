# CSV para TSV
# Faça um programa que abre o arquivo chamado dados.csv, em formato CSV, converte o conteúdo para o formato TSV e o salva em um arquivo dados.tsv.
# Um arquivo CSV representa dados em uma tabela nos quais os valores das colunas são separados por vírgula. Mais detalhes em: https://pt.wikipedia.org/wiki/Comma-separated_values.
# Um arquivo TSV também representa dados em uma tabela, com a diferença que ao invés de vírgulas os valores são separados por tabulações (caractere '\t').

with open("dados.csv") as file:
    content = file.readlines()
    
    with open("dados.tsv", "w") as data:
        for line in content:
            new_content = line.replace(",", "	")
            
            data.write(new_content)
