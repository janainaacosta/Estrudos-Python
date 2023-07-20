# introdução ao tipo de dados dict - dicionários

# dicionários - tipo de dado: par de "chave" e "valor"
# chaves podem ser consideradas "índices"

# usamos {} ou a classe 'dict' para criar dicionários

#imutáveis: str, int, float, bool, tuple
#mutáveis: dict, list

pessoa = {
    'nome': 'janaina',
    'sobrenome': 'costa', 
    'idade': 19, 
    'altura': 1.70,
    'endereco': [
        {'rua': 'dos bobos', 'numero': 0},
        {'rua': '1 de fevereiro', 'numero': 3}   
    ]
}

# pessoa = dict(nome = 'janaina', sobrenome = 'costa')

print(pessoa)
print (pessoa['nome'])

print()

for chave in pessoa:
    print(chave, pessoa[chave])
  