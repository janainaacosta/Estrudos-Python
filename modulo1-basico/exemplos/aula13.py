'''
Listas em python 
list - mutável
suporta valores de qualquer tipo
conhecimentos reutilizáveis - índices e fatiamento
métodos úteis: append, insert, pop, del, clear, extend, etc
'''

#........+01234
#........-54321
string = 'ABCDE'

#.........0.....1.......2.......3...4
#........-5....-4......-3......-2..-1
lista = [123, True, 'Janaina', 1.2, []]
lista[-3] = 'Maria'
print(lista[2]) #mostra "Maria" ao invés de "Janaina"

