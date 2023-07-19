'''
higher order functions - que podem receber/retornar outras funções
funçoes de 1° classe - tratadas como tipos de dados comuns (string, int...)
'''

def saudacao(msg, nome):
    return f'{msg}, {nome}'

def executa(funcao, *args):
    return funcao(*args)

# saudacao_2 = saudacao

v = executa(saudacao,'oi', 'ana')

print(v)