primeiro_valor = input("digite um numero: ")
segundo_valor = input("digite um numero: ")


if primeiro_valor > segundo_valor:
    maior = primeiro_valor
    menor = segundo_valor
else:
    maior = segundo_valor
    menor = primeiro_valor

print(f'{maior} é o maior valor \n{menor} é o menor valor')

