ano_nascimento = 1989
ano_formatura = 2010

# Considerando que as variáveis acima correspondem a 'Gerlaine', descubra a idade dela no ano da sua formatura
idade_formatura = ano_formatura - ano_nascimento
print(idade_formatura)

# Escreva expressões comparativas usando os operadores relacionais >, <= e ==. Imprima na tela as respostas
print(ano_nascimento < ano_formatura)
print(ano_nascimento == ano_formatura)
print(ano_nascimento == ano_formatura*ano_formatura)

# Crie expressões comparativas mais complexas utilizando operadores lógicos and, or e not. Imprima na tela as respostas

a = 20
b = 10
c = 30

print(a == 10 or b == 40)
print(a == c and b != 10)
print(a != c and not b != 10)