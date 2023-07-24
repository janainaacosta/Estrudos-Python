'shallow copy vc deepy copy em dados mutáveis'

# len - quantas chaves
# keys - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se chave não existir
# copy - retorna uma cópia rasa (shallow copy)
# get -  obtém uma chave
# pop - apaga um item com chave especf. (del)
#popitem - apaga último item adicionado
#update - atualiza um dicionário com outro

import copy

d1 = {
    # 'nome': 'janaina',
    # 'sobrenome': 'costa',
    # 'idade': 19
    'c1': 1,
    'c2': 2,
    'l1': [1, 2, 3]
}

# d2 = d1.copy()
d2 = copy.deepcopy(d1)


d2['c1'] = 1000
d2['l1'][1] = 90909

print(d1)
print(d2)