peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura**2)
print('O seu IMC é de: {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc <25:
    print('Peso Ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade morbida')
