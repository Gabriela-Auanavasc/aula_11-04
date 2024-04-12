
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
