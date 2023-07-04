'''
calculadora
'''
while True: 

    n1 = input('primeiro valor: ')
    n2 = input('segundo valor: ')
    operador = input('operador (+, -, x, /): ')

    numeros_validos = None
    n1_float = 0
    n2_float = 0

    try:
        n1_float = float(n1)
        n2_float = float(n2)
        numeros_validos = True

    except:
        numeros_validos = None
    if numeros_validos is None:
        print("Verifique se os números inseridos são válidos")
        continue
  
    operadores_permitidos ="+-/x"
    if operador not in operadores_permitidos:
        print("você precisa informar um dos operadores informados")
        continue

    if len(operador) > 1:
        print("informe apenas um operador")
        continue

    if operador == '+':
        resp = n1_float + n2_float
        print(resp)

    elif operador == '-':
        resp = n1_float - n2_float
        print(resp)

    elif operador == 'x':
        resp = n1_float * n2_float
        print(resp)

    elif operador == '/':
        resp = n1_float / n2_float
        print(resp)

    sair = input('Digite "s" para sair: ').lower().startswith('s')

    if sair is True:
        break