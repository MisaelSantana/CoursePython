"""
Loop for:

# Loop: Estruturas de repetição.
# For: Uma dessas estruturas.

# Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis.

# Exemplos  de iteráveis:
-> String:
    -> nome = 'Geek University'
-> Lista:
    -> lista = [1, 2, 3, 4, 5]
-> Range:
    -> numeros = (1, 10)
"""


nome = 'Geek University'
lista = [1, 2, 3, 4, 5]
numeros = (1, 10)

# Exemplo de for 1 (Iterando em uma string):
for letra in nome:
    print(letra)


# Exemplo de for 2 (Iterando em uma lista):
for numero in lista:
    print(numero)

"""
# Exemplo de for 3 (Iterando sobre uma range):
# range(valor_inicial, valor_final)
# OBS:
-> O valor final não é incluído(inclusive)
"""


nome = 'Geek University'
lista = [1, 2, 3, 4, 5]
numeros = (1, 10)


for numero in range(1, 10):
    print(numero)


# Enumerate:
for indice, letra in enumerate(nome):
    print(nome[indice])