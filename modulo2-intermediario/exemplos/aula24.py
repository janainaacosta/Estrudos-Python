'''
list comprehension com mais de um for 
'''

lista = []

for x in range(3):
    for y in range(3):
        print()
        lista.append((x, y))

'''lista = [
    (x, y) #o que vai ser incluído na lista nova - mapeamento
    for x in range(3)
    for y in range(3)
]'''

lista = [
    [x for y in range(3)]
    for x in range(3) # uma nova lista para cada x
]
 
print(lista)