# informanr nome
nome = input("informe seu nome: ")

# informar idade 
idade = input("informe sua idade: ")

#se os dois forem informados: 
if nome and idade:

    nome_invertido = nome[::-1]
    qtde_letras = (len(nome))
    if " " in nome:
        print('seu nome tem espaço')
    else:
        print('seu nome não tem espaço')

    print(
        f'seu nome é {nome}\n' 
        f'seu nome invertido é {nome_invertido}\n'
        f'seu nome tem {qtde_letras} letras\n'
        f'a primeira letra do seu nome é {nome[0]}\n'
        f'a última letra do seu nome é {nome[-1]}\n'
        )
else:
    print("você precisa informar seu nome e idade")