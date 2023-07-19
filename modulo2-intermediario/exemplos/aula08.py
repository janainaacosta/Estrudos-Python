'''
closure e funções que retornam outras funções 

'''

def cria_cumprimento(saudacao):
    def cumprimentar(nome):
        return f'{saudacao}, {nome}'
    return cumprimentar

saudar = cria_cumprimento('oi')
despedir = cria_cumprimento('tchau')

# print(saudacao_um('janaina'))
# print(despedir('janaina'))

for nome in ['ana', 'bia', 'cida', 'duda']:
        print(saudar(nome))
        print(despedir(nome))