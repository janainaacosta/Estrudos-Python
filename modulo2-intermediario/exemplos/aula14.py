'''
introdução ao tipo Set (conjuntos)
'''

"""
Sets em Python são mutáveis, mas aceitam apenas tipos imutáveis como valor interno

- eficientes para remover valor duplicado de iterável
- seus valores são sempre únicos
- não aceitam valores mutáveis
- não tem index
- não garantem ordem
- são iteráveis (for, in, not in)

métodos usáveis:
- add, update, clear, discart

operadores úteis:
- união '|' -> une
- intersecção '&' -> itens presentes em ambos
- diferença - itens presentes apenas no set da esquerda
- diferença simétrica '^' - itens que não estão em ambos
"""

# s1 = set('janaina', 1, 2, 3)
# print(s1)


s1 = set() # vazio
s1 = { 1, 2, 3, 3, 3, 3, 1}
print(s1)


#convertendo lista em set para remover valores repetidos 
# e revertendo para lista
l1 = [5, 6, 4, 5, 5, 6, (7, 8, 9,)]
s1 = set(l1)
print(s1)
print(3 not in s1)

s1 = list(l1)
print(s1)