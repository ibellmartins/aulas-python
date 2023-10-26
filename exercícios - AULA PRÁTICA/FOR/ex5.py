# 5)     Escreva um programa que exiba todos os números inteiros que são divisíveis por 3 e 7 ao mesmo tempo, no intervalo entre 1-100.

for n in range(1, 101):
    if n % 3 == 0 and n % 7 == 0:
          print(n)