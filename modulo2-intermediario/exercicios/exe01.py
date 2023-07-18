'''
Exercício - função

- crie uma função que multiplica todos os argumentos 
não nomeados recebidos
- retorne o total para uma variável e mostre o valor dela
'''

def multiplica(*args):
    total = 1 
    for numero in args:
        total *= numero
    return total

multiplica_paramentros = multiplica(2, 3, 3, 4, 5, 7)
print (multiplica_paramentros)