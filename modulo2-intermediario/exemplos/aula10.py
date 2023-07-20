'''
manipulando chaves e valores em dicionários 
'''
pessoa = {}
chave ='nome'

pessoa[chave] = 'janaina'
pessoa['sobrenome'] = 'costa'

# print(pessoa)
print(pessoa[chave],pessoa['sobrenome'])

print()

del pessoa['sobrenome']
print(pessoa)

print()

if pessoa.get('sobrenome') is None:
    print("['sobrenome'] não existe.")

else:
    print(pessoa['sobrenome'])