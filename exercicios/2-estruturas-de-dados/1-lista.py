# Crie uma lista apenas com elementos numéricos
lista_numerica = [0,1,2,3,4,5,6,7,8,9]
print(lista_numerica[2])

# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
lista_mista = [5,'Teste',2.5,[6,7,8], True]
print(lista_mista[1])

# Imprima na tela apenas os 5 primeiros elementos da lista
print(lista_numerica[:5])

# Crie um slice na lista para que imprima na tela os elementos de índice par
print(lista_numerica[::2])

# Remova da lista o último item
lista_numerica.pop()
print(lista_numerica)

# Insira na lista um novo item
lista_numerica.append(10)
print(lista_numerica)

# Remova da lista um item específico
lista_numerica.remove(4)
print(lista_numerica)