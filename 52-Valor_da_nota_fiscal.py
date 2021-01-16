# Valor da nota fiscal
# Faça uma função que recebe duas listas com informações de uma nota fiscal e devolve o preço total da nota. A nota fiscal é representada pelas duas listas, uma com preços de produtos e outra com a respectiva quantidade de itens comprados daquele produto.
# O nome da sua função deve ser calcula_total_da_nota.

def calcula_total_da_nota (prices, quantityes):
    total = 0
    
    i = 0
    while i < len(prices):
        price = prices[i]
        quantity = quantityes[i]
        
        total += price * quantity
        
        i += 1
        
    return total
