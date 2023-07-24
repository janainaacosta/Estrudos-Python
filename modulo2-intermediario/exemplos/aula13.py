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

p1 ={
    'nome': 'janaina',
    'sobrenome': 'costa'
}

print (p1["nome"])
print (p1.get("nome", "não existe"))

print(p1)
# nome = p1.pop('nome') # elimina a ultima chave 
# print (nome)
# print(p1)

# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

# p1.update({
#     'nome': 'novo nome'
#     'idade': 20
# })

# p1.update(nome= 'novo nome', idade=21)

# tupla = (('nome', 'novo valor'), ('idade', 30))
lista = [['nome', 'novo valor'], ['idade', 30]]
p1.update(lista)
print(p1)