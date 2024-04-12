
# O código abaixo é uma tentativa de criar um verificador de palíndromos.
# Palíndromos são palavras ou frases que são iguais quando lidas de trás para frente.
# No entanto, o código está incompleto e contém erros.
# Complete e corrija o código para que ele funcione corretamente.
# O usuário deve digitar uma palavra ou frase, e o programa deve imprimir se é um palíndromo ou não.
# Ignore espaços, pontuações e diferenças entre maiúsculas e minúsculas.

texto = input('digite um texto> ')
# uma string é tratada como uma sequencia de caracteres
# str[::-1] -> inversao de sequencia
texto_invertido = texto[::-1]

if texto == texto_invertido:
    print('> é um palíndromo!')
else:
    print('> não é um palíndromo.')
