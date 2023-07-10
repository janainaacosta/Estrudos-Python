'''
lista de compras com LISTA
--> o usuário deve ter a possibilidade de inserir, apagar e listar valores de sua lista.
--> não permita que o programa quebre com erros de índices inexistentes na lista
'''
import os

lista = []

while True:
    opcao = input("Selecione uma opção \n[i]nserir, [a]pagar, [l]istar: ")

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input('escolha um índice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('informe um número inteiro.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('erro desconhecido')

    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print("nada para listar")

        for i, valor in enumerate(lista):
            print(i, valor)

    else:
        print("insira uma opção válida.")