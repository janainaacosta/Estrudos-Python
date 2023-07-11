'''
split e join com list e str
split - divide uma string
join - une uma string
'''

frase = 'oi, bom dia'

lista_palavra_cruas = frase.split(',')

lista_palavra = []
for i, frase in enumerate(lista_palavra_cruas):
    lista_palavra.append(lista_palavra_cruas[i].strip())


# print(lista_palavra)

frases_unidas = ' - '.join(lista_palavra)
print(frases_unidas)
