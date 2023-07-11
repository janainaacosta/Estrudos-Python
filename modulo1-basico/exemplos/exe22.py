'''
lista de listas e seus índices 
'''

grupo = [
    ['arara', 'baleia', ],
    ['cachorro', 'doninha'],
    # ['elefante', 'formiga', (0, 1, 2, 3, 4)]
]

print(grupo[0][1])
# print(animais[2][2][3])

for animais in grupo:
    print(f'o grupo é {grupo}')
    for animal in animais:
        print(animal)