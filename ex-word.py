secret = 'banana'.upper()
result = len(secret) * '*'
cont = 0

while True:
    word = input('Informe uma letra:').upper()
    cont_word = len(word)
    cont += 1

    if cont_word > 1:
        print('Digite apenas uma letra')
        continue
    
    if cont_word < 1:
        print('Digite uma letra')
        continue
    
    if word in result:
        print('Já digitou esta letra')
        continue
    
    if (word in secret):
        i = 0
        temp = ''

        while (i < len(secret)):
            
            letter_secret = secret[i]
            letter_result = result[i]

            if word == letter_secret:
                temp += word
            elif letter_result != '*':
                temp += letter_result
            else:
                temp += '*'

            i += 1

        result = temp
        
    print(result)

    if secret == result:
        print(f'VENCEU A PALAVRA É "{result}"')
        print(f'Foram {cont} tentativas')
        cont = 0
        result = len(secret) * '*'
        break
    
