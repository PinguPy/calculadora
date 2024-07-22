
print('CALCULADORA SIMPLES EM PYTHON\n')

dicionario_de_operadores = {
    1: 'multiplicação',
    2: 'divisão',
    3: 'subtração',
    4: 'adição'
}

while True:
    for chave, valor in dicionario_de_operadores.items():
        print(f"{chave}: {valor}")
    print()  # Adiciona uma linha em branco

    seleção = int(input('Selecione uma das operações: '))
    print()  # Adiciona uma linha em branco

    if seleção == 1:
        print('MULTIPLIQUE\n')
        multiplicação = int(input('Primeiro número a multiplicar: ')) * int(input('Segundo número a multiplicar: '))
        resultado = multiplicação
        print('O resultado da sua operação é =', resultado)
        print()  # Adiciona uma linha em branco

    elif seleção == 2:
        print('DIVIDA\n')
        divisão = int(input('Primeiro número que deseja dividir: ')) / int(input('Segundo número a dividir: '))
        resultado = divisão
        print('O resultado da sua operação é =', resultado)
        print()  # Adiciona uma linha em branco

    elif seleção == 3:
        print('SUBTRAIA\n')
        subtração = int(input('Primeiro número que deseja subtrair: ')) - int(input('Segundo número a subtrair: '))
        resultado = subtração
        print('O resultado da sua operação é =', resultado)
        print()  # Adiciona uma linha em branco

    elif seleção == 4:
        print('SOME\n')
        adição = int(input('Primeiro número que deseja somar: ')) + int(input('Segundo número a somar: '))
        resultado = adição
        print('O resultado da sua operação é =', resultado)
        print()  # Adiciona uma linha em branco

    else:
        print('Escolha inválida. Por favor, tente novamente.')
        print()  # Adiciona uma linha em branco
        break

    continuar = input('Deseja realizar outra operação? (s/n): ').strip().lower()
    if continuar != 's':
        print('Obrigado por utilizar a calculadora Python de Pingu\n')
        break

