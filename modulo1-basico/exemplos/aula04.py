 # try | exception

numero = input("informe o numero: ")

try: 
    numero_int = int(numero)
    print("o dobro: ", numero_int * 2)
except:
    print("isso não é um número")
