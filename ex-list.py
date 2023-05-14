shopping = []

while True:
    option = input('[L]istar - [A]dicionar - [D]eletar : ').upper()

    if option == 'L':
        print(30 * '-')
        
        if len(shopping) > 0:
            for index, item in enumerate(shopping):
                print(f'{index} - {item}')
        else:
            print('LISTA VAZIA')

        print(30 * '-')

    elif option == 'A':
        item = input('nome do item: ').upper()
        shopping.append(item)

    elif option == 'D':
        index = input('informe o índice: ')
        
        if index.isdigit():
            index = int(index)

            if index <= len(shopping) - 1:
                shopping.pop(index)
            else:
                print('Indice não encontrado.')
                continue

        else:
            print('Indice inválido.')
            continue
    else:
        print('OPÇÃO INVÁLIDA')

