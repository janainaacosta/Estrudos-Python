'''
lista de listas e seus índices 
um pouco de desempacotamento
'''

grupo = [
    ['arara', 'baleia', ],
    ['cachorro', 'doninha'],
    # ['elefante', 'formiga', (0, 1, 2, 3, 4)]
]

print(grupo[0][1])
# print(animais[2][2][3])

for animais in grupo:
    print('o grupo é ', *grupo, end='\n')
    for animal in animais:
        print('animal desse grupo: ',animal)