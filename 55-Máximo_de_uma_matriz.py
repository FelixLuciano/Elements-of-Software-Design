# Máximo de uma matriz
# Escreva uma função que recebe uma matriz de tamanho 3×3 e devolve o maior valor absoluto dentre todos os seus elementos. A matriz é representada por uma lista de listas. Exemplo: a lista [[1, 2, 3], [4, 5, 6], [7, 8, 9]] representa a matriz
# \begin{pmatrix}1 & 2 & 3\\ 4 & 5 & 6\\ 7 & 8 & 9\end{pmatrix}
# Curiosidade: o maior valor absoluto encontrado em uma matriz é conhecido como a norma infinito dessa matriz.
# O nome da sua função deve ser 'encontra_maximo'.

def encontra_maximo (matrix):
    max_number = max([abs(num) for line in matrix for num in line])
                
    return max_number
