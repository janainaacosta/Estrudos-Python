'''
valores padrão para parâmetros 
- ao definif uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja 
enviado para o parâmetro, o valor padrão será usado
'''
#refatorar = editar o codigo 
 
def soma(x, y, z=None): # nesse caso, o parâmetro z foi definido como padrão
        if z is not None:
            print(f'{x=} {y=} {z=}', x + y + z)
        else:
            print(f'{x=} {y=}', x + y)

soma(1, 2)
soma(7, 8, 9)
