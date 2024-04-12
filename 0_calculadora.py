
# O código abaixo tem alguns problemas e está incompleto!
# Altere o código abaixo para que ele atue como uma calculadora
# O usuário deve digitar um valor, um operador e outro valor
# seu programa deverá imprimir na tela o resultado da operação
# Faça com que o seu programa funcione até que o usuário digite -1

mensagem = '>>> digite -1 para encerrar <<<'
print('\n', mensagem)
valor1 = float(input('digite um numero> '))
resultado = 0

while valor1 != -1:
    operador = input('escolha um operador> ')
    valor2 = float(input('digite o segundo numero> '))

    if valor2 == -1:
        break

    if operador == '+':
        resultado = valor1 + valor2
    elif operador == '-':
        resultado = valor1 - valor2
    elif operador == '*':
        resultado = valor1 * valor2
    elif operador == '/':
        if valor2 != 0:
            resultado = valor1 / valor2
        else:
            print('\n> erro; divisão por 0')
    else:
        print('\n> operador inválido')
        continue

    print('\n> resultado = ', resultado)
    print('---------------------')

    print('\n', mensagem)
    valor1 = float(input('digite um numero> '))
print('> calculadora encerrada.')
