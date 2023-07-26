'''
encontre o primeiro duplicado considerado 
a segunda ocorrência

requisitos: a ordem do número duplicado é considerada 
a partir da segunda ocorrência, ou seja, o número duplicado em si

exe.: [1, 2, 3, 3, 2, 1] -> o 1, 2, 3 são duplicados(retorne 3)
      [1, 2, 3, 4, 5, 6] -> não tem numero duplicado(retone -1)
'''

listas_de_listas = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4, 6, 5, 8, 1, 2, 9, 3, 7],
    [6, 1, 4, 9, 8, 2, 7, 3, 5],
    [5, 4, 2, 7, 6, 5, 3, 1, 4],
    [8, 6, 5, 8, 6, 2, 2, 8, 2], 
    [5, 6, 4, 3, 5, 7, 2, 4, 7]
]

def primeiro_duplicado(listas_de_listas):
    numeros_verificados = set()
    primeiro_duplicado = -1

    for numero in listas_de_listas:
        if numero in numeros_verificados:
             primeiro_duplicado = numero
             break

        numeros_verificados.add(numero)

    print()
    return primeiro_duplicado

for lista in listas_de_listas:
    print (
        lista, 
        primeiro_duplicado(lista)
    )

print(primeiro_duplicado([1, 2, 3, 3, 2, 1]))