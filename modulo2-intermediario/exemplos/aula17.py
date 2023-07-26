'''
exemplo de uso do Set
'''

letras = set()
while True:
    letra = input('digite: ')
    letras.add(letra)

    if 'v' in letras:
        print('era essa!')
        break

    print(letras)