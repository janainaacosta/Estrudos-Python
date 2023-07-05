'''
iterando strings com while
qual letra mais se repete?
'''

frase = 'sao paulo, 02 de julho de 2023' \
    'janaina costa da silva'.upper()

# print(frase.count('A'))

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    quantas_vezes_letra_apareceu = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < quantas_vezes_letra_apareceu:
        qtd_apareceu_mais_vezes = quantas_vezes_letra_apareceu
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(f'A letra que apareceu mais vezes foi "{letra_apareceu_mais_vezes}": {qtd_apareceu_mais_vezes}x')