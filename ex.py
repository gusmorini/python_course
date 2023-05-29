# ex 1

# number = input('Digite um número inteiro: ')

# try:
#   number_int = int(number)
#   if (number_int % 2 == 0):
#       print(f'O número {number_int} é par')
#   else:
#       print(f'O número {number_int} é impar')
# except:
#   print(f'"{number}" não é um número inteiro')


# ex 2

# hour = input('Infome a hora atual: ')

# try:
#   hour_int = int(hour)

#   if (hour_int >= 0 and hour_int <= 11):
#     print('BOM DIA')
#   elif (hour_int >= 12 and hour_int <= 17):
#     print('BOA TARDE')
#   elif hour_int >= 18 and hour_int <= 23:
#     print('BOA NOITE')
#   else:
#     print('Hora deve ser entre 0 e 23')
    
# except:
#    print(f'"{hour}" não é uma hora válida')   

# EX 3

name = input('Informe seu primeiro nome: ')
cont = len(name)

if (cont >= 1):
  if (cont <= 4):
    print('Seu nome é curto')
  elif (cont >= 5 and cont <= 6):
    print('Seu nome é normal')
  else:
    print('Seu nome é muito grande')
else:
  print('Digite pelo menos uma letra!')