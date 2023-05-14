import random

# populando 9 digitos

nove_digitos = ''
for _ in range(9):
     nove_digitos += str(random.randint(0,9))

# digito 1

regressivo_1 = 10
total_1 = 0
for digito in nove_digitos:
    total_1 += (int(digito) * regressivo_1)
    regressivo_1 -= 1

resto_1 = (total_1 * 10) % 11
digito_1 = resto_1 if resto_1 <= 9 else 0

# digito 2

dez_digitos = nove_digitos + str(digito_1)
regressivo_2 = 11
total_2 = 0
for digito in dez_digitos:
     total_2 += int(digito) * regressivo_2
     regressivo_2 -= 1

resto_2 = total_2 * 10 % 11
digito_2 = resto_2 if resto_2 <= 9 else 0

cpf_gerado = (f'{nove_digitos}{digito_1}{digito_2}')

print(f'CPF gerado: {cpf_gerado}')
     