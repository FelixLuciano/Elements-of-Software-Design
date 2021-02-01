# Login disponível
# Este exercício caiu na avaliação final de Design de Software 2019-2
# Você está trabalhando em um processo de migração de um sistema de gestão antigo para uma nova versão mais robusta. Nessa nova versão os nomes de usuários (login) devem ser únicos. Como essa restrição não existia na versão anterior, há alguns usuários com o mesmo login.
# Para resolver esse problema, logins iguais devem ser acrescidos de um número crescente no final. Por exemplo, se os logins 'andrek', 'andrek1', 'andrek2' já existem no sistema ao tentarmos adicionar um novo usuário chamado 'andrek', ele deve ser renomeado para 'andrek3'.
# Faça uma função que recebe um login de usuário, representado por uma string, e uma lista de logins já existentes no sistema, representada por uma lista de strings. Se o login do usuário não existe na lista, ele é devolvido sem modificações. Caso contrário, sua função deve devolver o próximo login disponível.
# Exemplos:
# - login_disponivel('lucio', ['andre', 'fabio']) deve devolver 'lucio'
# - login_disponivel('lucio', ['andre', 'fabio', 'lucio']) deve devolver 'lucio1'
# - login_disponivel('lucio', ['andre', 'fabio', 'lucio', 'lucio1']) deve devolver 'lucio2'
# Você pode assumir que os logins de usuários inicialmente não possuem dígitos no final e que a lista de logins no sistema não pula nenhum número. Ou seja, não vai existir um 'lucio3' na lista se não existir um 'lucio', 'lucio1' e 'lucio2'.
# O nome da sua função deve ser 'login_disponivel'.
