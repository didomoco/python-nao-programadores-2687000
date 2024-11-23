# Criaremos um script que imprimirá na tela o total de horas que uma pessoa estudou durante um determinado período:
# 1. Crie uma variável chamada "nome" e, usando o método input(), atribua a ela um nome;
nome = input ('Informe o seu nome:  ')

# 2. Crie uma variável chamada "total_dias" e, usando o método input(), solicite o total de dias dedicados ao estudo por semana;
total_dias = input('Dias de estudo: ')

# 3. Crie uma variável chamada "total_horas" e, usanod o método input(), solicite a média de horas estudada por dia;

total_horas = input('Horas de estudo: ')

# 4. Crie uma variável chamada "curso" e, usando o método input(), solicite o título do curso desejado;

Curso = input('Curso desejado: ')

# 5. Imprima na tela uma frase informando o nome da estudante, o total_dias dedicados aos estudos, o total horas semanais e o curso.

total_dias = int(total_dias)
total_horas= int(total_horas)

print (f"Olá, {nome}! O total de dias de estudo é {total_dias}  e o total de horas por dia de estudo é {total_horas}. Isso equivale a {total_horas*total_dias} horas por semana. Insufuciente se quiser passar no curso de {Curso}. Presta atenção!")