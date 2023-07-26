'''
MÉTODOS ÚTEIS DO TIPO SET

métodos usáveis:
- add, update, clear, discart

operadores úteis:
- união '|' -> une
- intersecção '&' -> itens presentes em ambos
- diferença - itens presentes apenas no set da esquerda
- diferença simétrica '^' - itens que não estão em ambos
'''

s1 = set()
s1.add('janaina')
s1.add('costa')
print(s1)
s1.clear()
s1.update(('silva', 1, 2, 3 ))
print(s1)

s1.discard('silva')
print(s1)
