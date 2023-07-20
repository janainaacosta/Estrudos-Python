'''
métodos úteis nos dicionários 
'''
# len - quantas chaves
# keys - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se chave não existir
# copy - retorna uma cópia rasa (shallow copy)
# get -  obtém uma chave
# pop - apaga um item com chave especf. (del)
#popitem - apaga último item adicionado
#update - atualiza um dicionário com outro

pessoa = {
    'nome': 'janaina',
    'sobrenome': 'costa', 
    'sobrenome': 'da silva',
    'idade': 19, 
    'altura': 1.70,
    
}

pessoa.setdefault('endereco', 'brasil')
print(pessoa['endereco'])

# print(pessoa.__len__())
# print(len(pessoa)) # mostra a quantidade de chaves 
# print(list(pessoa.keys())) # mostra as chaves 
# print(list(pessoa.values())) # mostra os valores das chaves 
print(list(pessoa.items())) 

# for valor in pessoa.values():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)