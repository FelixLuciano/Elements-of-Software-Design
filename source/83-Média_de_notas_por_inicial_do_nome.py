# Média de notas por inicial do nome
# Existe uma suspeita do laboratório SpuriousCorrelations de que a letra inicial do nome de um aluno influencia em seu desempenho acadêmico. Faça uma função que recebe um dicionário de notas cujas chaves são os nomes dos alunos. A função deve devolver um novo dicionário com as médias das notas dos alunos para cada letra inicial. Exemplo:
# Entrada: {'Andrew Ayres': 6, 'Fábio Ikeda': 10, 'Fábio Kurauchi': 9, 'Raul Hage': 8}
# Saída: {'A': 6, 'F': 9.5, 'R': 8}
# O nome da sua função deve ser 'medias_por_inicial'.

def grades_in_initial (students):
    grades = {}
    
    for name, student_grades in students.items():
        initial = name[0]
        
        if not initial in grades:
            grades[initial] = [student_grades]
        else:
            grades[initial].append(student_grades)
        
    return grades

def medias_por_inicial (students):
    grades_avegare = {}
    
    for initial, grades in grades_in_initial(students).items():
        grade_average = sum(grades) / len(grades)
        
        grades_avegare[initial] = grade_average
        
    return grades_avegare
