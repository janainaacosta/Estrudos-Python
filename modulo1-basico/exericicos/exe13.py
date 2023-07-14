# ALGORITMO DO CPF

'''
CALCULO DO PRIMEIRO NUMERO DO DÍGITO: 
soma dos 9 primeiros n° em uma contagem regressiva começando do 10

'''

cpf_inserido = input('Informe o número de CPF: ')


cpf_inserido .replace('.', '') \
    .replace('-', '')
print(cpf_inserido)
    
nove_digitos = cpf_inserido [:9]
contagem_regressiva_1 = 10

resultado_digito1 = 0

for digito in nove_digitos:
    resultado_digito1 += int(digito) * contagem_regressiva_1
    contagem_regressiva_1 -= 1

digito1 = (resultado_digito1 * 10) % 11
digito1 = digito1 if digito1 <= 9 else 0

dez_digitos = nove_digitos + str(digito1)
contagem_regressiva_2 = 11

resultado_digito2 = 0

for digito in dez_digitos:
    resultado_digito2 += int(digito) * contagem_regressiva_2
    contagem_regressiva_2 -= 1

digito2 = (resultado_digito2 * 10) % 11
digito2 = digito2 if digito2 <= 9 else 0


cpf_validado = f"{nove_digitos}{digito1}{digito2}"


if cpf_validado == cpf_inserido:
    print("CPF válido")

else:
    print("CPF inválido")