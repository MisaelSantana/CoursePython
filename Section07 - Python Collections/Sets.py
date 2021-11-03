"""
Conjuntos:

# Conjuntos em qualquer linguagem de programação, estamos fazendo referência
à Teoria dos Conjuntos da matemática.

# Aqui em Python, os conjuntos são chamaos de Sets.

# Dito isto, da mesma forma que na matemática:
-> Sets (conjuntos) não possuem valores duplicados;
-> Sets (conjuntos) não possuem valores ordenados;
-> Elementos não acessados via índice, ou seja, conjuntos não são indexados;

# Conjuntos são bons quando:
-> Rrecisamos armazenar elementos mas não nos importamos com a ordenação deles.
-> Quando não precisamos se preocupar com chaves, valores e itens duplicados.

# Os conjuntos (sets) são referenciados em Python com chaves: {}

# Diferença entre conjuntos (Set) e Mapas (Dicionários) em Python:
-> Um dicionário tem chave/valor;
-> Um conjunto tem apenas valor;
"""


# Definindo um conjunto:

# Forma 1:
s = set({1, 2, 3, 4, 5, 6, 7, 5, 2, 3}) # Repare que temos valores repetidos:

print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado
# sem gerar erro e não fará parte do conjunto.

# Forma 2:
s = {1, 2, 3, 4, 5, 5}

print(s)
print(type(s))

# Podemos verificar se determinado elemento está contido no conjunto:
if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')


# Importante lembrar que além de não termos valores duplicados,
# não temos ordem:

# Listas aceitam valores duplicados, então temos 10 elementos.
lista = [99, 2, 34, 23, 12, 1, 44, 5, 2, 34]
print(f'Lista: {lista} com {len(lista)} elementos')

# Tuplas aceitam valores duplicados, então temos 10 elementos.
tupla = 99, 2, 34, 23, 12, 1, 44, 5, 2, 34
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# Dicionários não aceitam chaves duplicadas, por isso temos 8 elementos.
dicionario = {}.fromkeys([99, 2, 34, 23, 12, 1, 44, 5, 2, 34], 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')

# Conjuntos não aceitam valores duplicados, por isso temos 8 elementos.
conjunto = {99, 2, 34, 23, 12, 1, 44, 5, 2, 34}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')


# Assim como todo outro conjunto Python, podemos colocar tipos de dados misturados em Sets
s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))


# Podemos iterar em um set normalmente:
for valor in s:
    print(valor)


# Usos interessantes com sets:
"""
# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu
e os visitantes informaram manualmente a cidade de onde vieram.

# Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos
e ter repetição
"""


cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']

print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos.
print(len(set(cidades)))


# Adicionamos elementos em um conjunto:
s = {1, 2, 3}

s.add(4)
print(s)

# Remover elementos em um conjunto:

# Forma 1:
s = {1, 2, 3}
print(s)

s.remove(3)
print(s)

# OBS: Caso o valor não seja encontrado, será gerado o erro KeyError

# Forma 2:
s = {1, 2, 3}
print(s)

s.discard(2)
print(s)

# OBS: Se o valor não for encontrado, nenhum erro é gerado.


# Copiando um conjunto para outro:

# Forma 1: -> # Deep Copy
s = {1, 2, 3}

novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)