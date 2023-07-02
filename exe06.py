horario = input("Informe o horário: ")

try:
    horario_int = int(horario)

    if horario_int > 0 and horario_int < 12 :
        print("Bom dia :) ")
    elif horario_int >= 12 and horario_int < 18 :
        print("Boa tarde :) ")
    elif horario_int >= 18 :
        print("Boa noite :) ")
    else:
        print("informe apenas inteiros de 0-23")

except:
    print("Deve ser um número inteiro")