'tuplas'

# tuplas são imutáveis.

nomes = 'A', 'B', 'C', 'D', 'E' # forma 1
nomes = tuple(nomes)            # forma 2

_, _, nome, *resto =  nomes

print(' ')
print(nome)
