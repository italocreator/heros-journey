# def parouimpar(a):
#     if a % 2 == 0:
#         return ('Par')
#     else:
#         return ('Impar')


# num = int(input('Digite um numero: '))
# print(parouimpar(num))


def maior(num, num2, num3):
    if num > num2 and num > num3:
        print(f'{num} é o maior de todos')
    elif num2 > num and num2 > num3:
        print(f'{num2} é o maior de todos')
    else:
        print(f'{num3} é o maior de todos')


maior(num=int(input('Digite um numero: ')),
      num2=int(input('Digite um numero: ')),
      num3=int(input('Digite um numero: '))
      )
