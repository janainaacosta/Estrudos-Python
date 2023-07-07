'''
dados mutáveis
--> copiando o valor (imutáveis)
--> aponta para o mesmo valor na memória (mutável)
'''

nome = 'janaina'
valor_anterior = nome
nome = 'anianaj'

print(valor_anterior)
print(nome)


print("--------------------------------------")

lista_a = ["amora", "baixinho", 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'qualquer coisa'
print(lista_a)
print(lista_b)