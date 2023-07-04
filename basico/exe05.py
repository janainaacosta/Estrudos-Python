num = input("Informe um valor inteiro: ")

try:
    num_int = int(num)

    if  num_int % 2 == 0:
        tipo_num = 'par'
    elif num_int % 2 == 1:
        tipo_num = 'ímpar'

    print(tipo_num)

except:
    print("O número informado não é inteiro")



