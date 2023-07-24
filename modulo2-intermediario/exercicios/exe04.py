'''
SISTEMA DE PERGUNTAS E RESPOSTAS 
'''

perguntas = [
    {
        'pergunta': 'qual é sigla de Brasilia?',
        'opcoes': ['bra', 'brl', 'bsb', 'bsl'],
        'resposta' : 'bsb'
    },
    {
        'pergunta': 'qual o menor osso do corpo humano?',
        'opcoes': ['estribo', 'cuboide', 'manúbrio', 'ísquio'],
        'resposta' : 'estribo'
    },
    {
        'pergunta': 'quando michelangelo morreu?',
        'opcoes': ['1378', '1564', '1731', '1406'],
        'resposta' : '1564' 
    }
]

num = 1

qtde_acertos = 0
for pergunta in perguntas:
    print(num, ')', pergunta['pergunta'])
    num += 1
    print()

    opcoes = pergunta['opcoes']
    for i,  opcao in enumerate(opcoes):
        print(i, ')',opcao)

    resposta = input('---> ')

    acertou = False
    resposta_int = None
    qtde_opcoes = len(opcoes)

    if resposta.isdigit():
        resposta_int = int(resposta)

    if resposta_int is not None:
        if resposta_int >- 0 and resposta_int < qtde_opcoes:
            if opcoes[resposta_int] == pergunta['resposta']:
                acertou = True
    print()
    if acertou:
        print('resposta certa')
        qtde_acertos += 1
    else:
        print('resposta incorreta')
    print()


print('você acertou', qtde_acertos, ' de ', len(perguntas))
