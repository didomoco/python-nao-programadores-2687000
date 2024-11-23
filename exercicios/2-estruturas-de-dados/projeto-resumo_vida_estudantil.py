# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica

estudante = {}
estudante['nome'] = str(input("Quem é você?"))
estudante['ano_linkedin'] = int(input ("Ano que conheceu a ferramenta: "))
estudante['ano_atual'] = int(input ("Ano atual: "))
cursos = input("Cursos realizados(separar por .): ")
estudante['cursos'] = cursos.split(', ')
#print(estudante)

# 2. Armazene esses dados em um dicionário
# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.

anos_transcurridos = estudante['ano_atual'] - estudante['ano_linkedin']
total_cursos = len(estudante['cursos'])

print (f"Olá {estudante['nome']}, você conheceu a ferramenta em {estudante['ano_linkedin']}, ou seja, já tem {anos_transcurridos} anos. Parabéns por realizar {total_cursos} cursos na plataforma! Destaco aqui o primeiro curso sobre: {estudante['cursos'][0]}. Assim como o mais recente: {estudante['cursos'][-1]}")