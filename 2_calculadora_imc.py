
# O código abaixo é uma tentativa de criar uma calculadora de Índice de Massa Corporal (IMC).
# No entanto, ele está incompleto e contém erros.
# Modifique o código para que ele solicite ao usuário seu peso em quilogramas e altura em metros.
# Seu programa deve calcular e imprimir o IMC do usuário seguindo a fórmula IMC = peso / (altura ** 2).
# Além disso, deve classificar o resultado em: Baixo peso, Peso normal, Sobrepeso ou Obesidade, 
# baseando-se nos valores de IMC.

peso = float(input('digite seu peso em kg> '))
altura = float(input('digite sua altura em metros> '))

imc = peso /(altura * 2)

# classificação do IMC
if imc < 18.5:
    classificacao = '> baixo peso'
elif imc > 18.5 and imc < 24.9:
    classificacao = '> peso nomal'
elif imc >= 25 and imc < 29.9:
    classificacao = '> sobrepeso'
else:
    classificacao = '> obesidade'
print(f"> seu IMC é {imc:.1f} e sua classificação é: {classificacao}")
