'''
introdução à função lambda + list.sort e sorted

- lambda é uma função normal como as outras. Porém, são funções 
anônimas que contém apenas uma linha, ou seja, tudo deve ser contido
dentro de uma única expressão.
'''
lista = [
    {'nome': 'janaina', 'sobrenome': 'costa'},
    {'nome': 'anianaj', 'sobrenome': 'atsoc'},
    {'nome': 'costa', 'sobrenome': 'janaina'},
    {'nome': 'atsoc', 'sobrenome': 'anianaj'}
]


# lista = [3, 6, 4, 9, 5, ]
# lista.sort(reverse=True)

# def ordena(item):
#     # print('print', item)
#     return item['nome'] # substituido

def exibir(lista):
    for item in lista:
        print(item)
    print() 

# lista.sort(key=lambda item:item['nome'])
l1 = sorted(lista, key=lambda item:item['nome'])
l2 = sorted(lista, key=lambda item:item['sobrenome'])
# print(lista) 

# for item in lista:
#     print(item)

exibir(l1)
exibir(l2)