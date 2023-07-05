'''
 while - condição em detalhes

 - break / continue 
'''

contador = 0

while contador < 100 :   
    contador += 1

    if contador == 6:
        print("Não vou mostrar o 6")
        continue

    if contador >= 10 and contador <= 30:
        continue #não vai mostrar nada entre esses números

    print(contador)

    if contador == 40:
        break

print('acabou')