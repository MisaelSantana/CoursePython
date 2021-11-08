"""
Min e Max:

# max():
-> Retorna o maior valor em um iterável ou o maior de dois ou mais elementos;

# min():
-> Retorna o menor valor em um iterável ou o menor de dois ou mais elementos;

"""


# Exemplo de uso simples:

# Lista:
lista = [32, 8, 4, 99, 34, 129]

print(max(lista))  # 129
print(min(lista))  # 4

# Tupla:
tupla = (32, 8, 4, 99, 34, 129)

print(max(tupla))  # 129
print(min(tupla))  # 4

# Conjunto:
set = {32, 8, 4, 99, 34, 129}

print(max(set))  # 129
print(min(set))  # 4

# Dicionário:
dict = {'a': 32, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}

print(max(dict))  # f
print(min(dict))  # a
# Imprimindo os valores:
print(max(dict.values()))  # 129
print(min(dict.values()))  # 4
