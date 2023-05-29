text = 'BAnanA 123 testando a frase'.upper()

i = 0
qtd = 0
result = ''
tested = ''
characters = ' .!+-/,@$%#?[]`´'

while i < len(text):
    letter = text[i]
    i += 1

    if letter in characters or letter in tested:
        continue
        
    tested += letter
    count_letter = text.count(letter)

    if count_letter > qtd:
        qtd = count_letter
        result = letter

print(f'A letra "{result}" apareceu {qtd}x na frase: "{text}"')