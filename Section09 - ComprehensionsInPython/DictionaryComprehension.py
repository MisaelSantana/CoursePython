"""
Dictionary Comprehension:

# Pense no seguinte:

-> Se quisermos criar uma lista fazemos:
lista = [1, 2, 3, 4]

-> Se quisermos criar uma tupla fazemos:
tupla = (1, 2, 3, 4)

-> Se quisermos criar um set(conjunto) fazemos:
set = {1, 2, 3, 4}

-> Se quisermos criar um dicionário fazemos:
dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# Sintaxe:
{chave:valor for valor in iterável}

"""


# Exemplos

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

quadrado = {chave:valor ** 2 for chave, valor in numeros.items()}
print(quadrado)