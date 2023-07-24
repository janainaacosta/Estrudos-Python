'''
criar função que duplica, tripica e quadruplica
o n° recebido como parametro 
'''

def cria_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar
    
duplica = cria_multiplicador(2)
triplica = cria_multiplicador(3)
quadruplica = cria_multiplicador(4)
 
numero_escolhido = input("escolha um valor: ")
numero_escolhido_int = int(numero_escolhido)

print(duplica(numero_escolhido_int))
print(triplica(numero_escolhido_int))
print(quadruplica(numero_escolhido_int))
