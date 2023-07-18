'''
- crie uma função que mostra se um numero é
 impar/par e retorne
'''


def par_ou_impar(a):
    tipo = ''

    if a % 2 == 0:
        tipo = 'Par'
    else:
        tipo = 'Ímpar'
    
    return tipo

tipo_de_parametro = par_ou_impar(3)
print(tipo_de_parametro)
