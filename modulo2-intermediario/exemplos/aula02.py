'''
- argumentos nomeados e não nomeados em funçoes python
- argumentos nomeados tem nome com sinal de igual
- argumento não nomeado recebe apenas o argumento (valor)
'''

def soma(x, y, z):
    print(f'{x=}  y={y} z= {z}', '|', 'x + y = ', x + y)

soma(2, 3, z = 5)