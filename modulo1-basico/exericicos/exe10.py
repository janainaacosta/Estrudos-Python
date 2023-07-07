'''
ACERTE A PALAVRA

- propor uma palavra e o usuarío deve informar uma letra por vez
- caso o usuário erre a letra, mostrar * no local onde deveriam estar as letras
- fazer contagem de tentativas
'''

palavra = 'edredom'
palavra_ocultada = ''
jogadas = 0

while True:
    tentativa_letra = input('Informe uma letra: ')

    jogadas += 1

    if len(tentativa_letra) > 1:
        print("Informe apenas uma letra")
        continue

    contador = 0

    while contador < len(palavra):
        palavra_ocultada += '*'
        contador += 1

    i = 0
    palavra_revelada = ''

    while i < len(palavra):
        letra = palavra[i]

        if letra == tentativa_letra:
            palavra_revelada += tentativa_letra
        else:
            palavra_revelada += palavra_ocultada[i]

        i += 1

    palavra_ocultada = palavra_revelada
    print(palavra_ocultada)

    if palavra_revelada == palavra:
        print(f'Exato! a palavra é: {palavra}. \nTotal de jogadas: {jogadas}')
        break