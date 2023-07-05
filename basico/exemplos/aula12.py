# as coisas do while funcionam no for

for i in range(10):
    if i == 2:
        print('pulando o 2')
        continue

    if i == 6:
        print('i é 8,seu else não executará')
        break
    for j in range(1, 3):
        print(i, j)

else: 
    print('For completo!')