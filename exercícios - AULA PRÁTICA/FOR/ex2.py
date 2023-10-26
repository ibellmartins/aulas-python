'''
2)  Faça um programa que exiba na tela os 20 primeiros números quadrados perfeitos, da seguinte forma:
1 ** 2 = 1
2 ** 2 = 4
3 ** 2 = 9
4 ** 2 = 16
'''

for num in range(1, 21):
    quad = num**2
    print(f'{num} ** 2 = {quad}')   #importante: pro laço ser executado por inteiro o print deve estar dentro do FOR 
