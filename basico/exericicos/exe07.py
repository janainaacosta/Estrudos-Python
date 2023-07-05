nome = input("Informe seu nome: ")

try:

    qtde_letras = len(nome)

    if qtde_letras <= 4:
        print("Seu nome é curto")
    elif qtde_letras > 4 and qtde_letras <= 6:
        print("Seu nome é normal")
    elif qtde_letras > 6:
        print("Seu nome é muito grande")

except:
    print("Informe um nome válido")