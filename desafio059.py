from math import factorial
n1 = int(input('Escolha um numero: '))

n2 = int(input('Escolha um numero: '))

opcao = 0
 
while opcao != 8:

    print('=-=' * 10)
    print('''
        MENU DE OPÇÕES

    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] SUBTRAÇÃO
    [ 4 ] DIVISÃO
    [ 5 ] MAIOR
    [ 6 ] FATORIAL DE UM DOS NÚMEROS
    [ 7 ] NOVOS NÚMEROS
    [ 8 ] SAIR DO PROGRAMA
    ''')
    print('=-=' * 10)
    acao = int(input('>>>>> Qual opção deseja acessar? '))

    if acao == 1:

        print(f'O resultado da soma dos números {n1} e {n2} é {n1 + n2}')

    elif acao == 2:

        print(f'O resultado da multiplicação dos números {n1} e {n2} é {(n1 * n2):.2f}')

    elif acao == 3:

        print('''Ordem dos fatores disponíveis:

                [ 1 ] n1 - n2
                [ 2 ] n2 - n1
        ''')

        ordemdosfatores = int(input('Qual das ordens de fatores deseja seguir:'))

        if ordemdosfatores == 1:

            print(f'O resultado da subtração entre {n1} e {n2} é {n1 - n2}')

        elif ordemdosfatores == 2:

            print(f'O resultado da subtração entre {n2} e {n1} é {n2 - n1}')

    elif acao == 4:

        print('''Ordem dos fatores disponíveis:

                        [ 1 ] n1 / n2
                        [ 2 ] n2 / n1
                ''')

        ordemdosfatores = int(input('Qual das ordens de fatores deseja seguir:'))

        if ordemdosfatores == 1:

            print(f'O resultado da subtração entre {n1} e {n2} é {n1 / n2}')

        elif ordemdosfatores == 2:

            print(f'O resultado da subtração entre {n2} e {n1} é {n2 / n1}')

    elif acao == 5:

        if n1 > n2:

            print(f'O numero {n1} é maior do que o numero {n2}')

        elif n1 < n2:

            print(f'O numero {n2} é maior do que o numero {n1}')

        elif n1 == n2:

            print(f'Os números {n1} e {n2} são iguais')

    elif acao == 6:

        print(f'''
                Qual dos fatores você deseja obter a fatorial?
                
                [ 1 ] n1 = {n1}
                [ 2 ] n2 = {n2}
''')
        fatorial = int(input('Qual das opções deseja realizar: '))

        if fatorial == 1:

            f1 = factorial(n1)

            print(f'O Fatorial de {n1} é {f1}!')

        elif fatorial == 2:

            f2 = factorial(n2)

            print(f'O Fatorial de {n2} é {f2}!')

    elif acao == 7:

        print('Informe os números novamente:')

        n1 = float(input('Escolha um numero: '))

        n2 = float(input('Escolha um numero: '))

    elif acao == 8:

        print('Finalizando serviços...')
        break

    else:

        print('Opção invalida, tente novamente!')

print('Fim do programa, volte sempre!')