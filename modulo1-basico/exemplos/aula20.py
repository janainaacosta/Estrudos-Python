"""
enumerate para numerar valores de iteráveis
"""

lista = ['australia', 'brasil', 'croacia']
lista.append('dominica')

lista_enumerada = enumerate(lista)

for item in lista_enumerada:
    print(item)