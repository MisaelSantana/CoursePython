"""
Sorted(ordenar):

# OBS:
-> Não confunda, apesar do nome, com a função sort() que já estudamos em listas;
-> O sort(), só funciona em listas.
-> O sorted(), SEMPRE retorna uma Lista com os elementos do iterável ordenados.

# Podemos utilizar o sorted() com qualquer iterável.

# Como o próprio nome diz, sorted() serve para ordenar
"""


# Exemplo:
numeros = [6, 1, 8, 3, 5, 2, 5]
print(numeros)

print(sorted(numeros))

print(numeros)


# Ordenando do maior para o menor:
numeros = [6, 1, 8, 3, 5, 2, 5]
# Adicionando parâmetros ao sorted()

print(sorted(numeros, reverse=True))
