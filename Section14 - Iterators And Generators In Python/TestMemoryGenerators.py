"""
Teste de memória com Generators:

# 
"""


# Exemplo:

def fib_lista(max):
    nums = []
    a, b, = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums

# Teste
for n in fib_lista(100000):
    print(n)
