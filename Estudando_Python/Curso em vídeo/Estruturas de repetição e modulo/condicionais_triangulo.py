ladoa = float(input('Digite o primeiro segmento: '))
ladob = float(input('Digite o segundo segmento: '))
ladoc = float(input('Digite o terceiro segmento: '))
if ladoa < ladob + ladoc and ladob < ladoa + ladoc and ladoc < ladoa + ladob:
    print('Os segmentos acima PODEM formar um triângulo!')
    if ladoa == ladob and ladoc == ladoa:
        print('EQUILATERO')
    if ladoa != ladob != ladoc != ladoa:
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO')
