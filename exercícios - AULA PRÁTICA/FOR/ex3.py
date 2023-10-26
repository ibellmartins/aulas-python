'''
3) Escreva um programa que exiba os números pares, partindo de 2 até atingir um valor x informado pelo teclado. Se o valor informado for um número ímpar, então devem ser exibidos os números ímpares, partindo de 1 até atingir esse valor. Exemplos:

Valor de X = 14 è 2 4 6 8 10 12 14
Valor de X = 17 è 1 3 5 7 9 11 13 15 17
'''

num = int(input('digite um numero inteiro: '))
if num % 2 == 0:
    for num in range(2, num+1, 2):
        print(num)
else: 
    for num in range(1, num+1, 2):
        print(num)
        