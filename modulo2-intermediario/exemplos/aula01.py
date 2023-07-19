'''
funções
'''

def imprimir (a, b, c):
    print('aa')
    print('bb')
    print('cc')

imprimir(1, 2, 3)

print('')

def imprimir_2 (a, b, c):
    print(a, b, c)

imprimir_2(1, 2, 3)
imprimir_2(4, 5, 6)

print('')

def saudacao(nome = 'desconhecido'):
    print(f'olá, {nome}.')

saudacao('arara')
saudacao('baleia')
saudacao('cachorro')
saudacao()