'''
iterando strings com while
'''
nome = "Janaina"

contador = 0
nome_novo = " "

while contador < len(nome):
    letras = nome[contador]
    nome_novo += letras
    nome_novo += "~"
    contador += 1
print(nome_novo)