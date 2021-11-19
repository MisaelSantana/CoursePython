"""
Forçando tipos de dados com decoradores:

# 
"""


# Exemplo:
def forca_tipo(*tipos):
    def decorador(funcao):
        def converte(*args, **kwargs):
            novo_args = []
            for(valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))  # str('Misael'), int(5)
            return funcao(*novo_args, **kwargs)
        return converte
    return decorador


@forca_tipo(str, int)
def repete_msg(msg, vezes):
    for vez in range(vezes):
        print(msg)

repete_msg('Misael', '5')
repete_msg('Misael', 5)


@forca_tipo(float, float)
def dividir(a, b):
    print(a / b)

dividir('1', '5')
dividir(1, 5)
