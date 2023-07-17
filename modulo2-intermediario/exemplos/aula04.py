'''
escopo de funções em python

escopo: local onde o código pode atingir 
global: todo o código é alcançável
local: nomes do mesmo local podem ser alcançados
'''

x = 1

def escopo():
    global x
    x = 10

    def outra_funcao():
            x = 11
            y = 2
            print(x, y)

    outra_funcao()
    # print(x)

# print(x) # execulta antes de chamar a função. X ainda é 1
escopo() # chama a função, define como global e altera o valor para 10
# print(x)