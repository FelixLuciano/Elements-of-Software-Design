# Lista alunos ímpares
# Escreva uma função que recebe uma lista de nomes de alunos e devolve uma lista contendo somente os alunos nos índices ímpares, dividindo a turma em dois.
# O nome da sua função deve ser 'alunos_impares'.

def alunos_impares (students):
    return [student for i, student in enumerate(students) if bool(i % 2)]
