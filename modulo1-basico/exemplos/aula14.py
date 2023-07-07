'''
Listas em python 
list - mutável
suporta valores de qualquer tipo
conhecimentos reutilizáveis - índices e fatiamento
métodos úteis: append, insert, pop, del, clear, extend, etc

------> CRUD
'''


lista = [10, 20, 30, 40]
print(lista)

numero = lista[2]
print('valor 2 da lista: ', numero)

lista[1] = 300
print('mudou o primeiro valor da lista para 300: ', lista)

print('mostra o atual 2 valor da lista', lista[2])

del lista[3]
print('após deletar o 3° valor da lista: ', lista)

lista.append(50)            #adiciona um valor no final
lista.append(100)           #adiciona um valor no final
ultimo_valor = lista.pop()  #remove o valor no final
print('após remover o último valor da lista: ', ultimo_valor)
lista.append(200)           #adiciona um valor no final
quarto_valor = lista.pop(3)
print('após remover o quarto valor da lista: ', quarto_valor)
print(lista)

lista.insert(0, '0') # (indice, valor) -> adiciona um valor no início da lista