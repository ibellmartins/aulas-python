'''
4)  Faça um programa que exiba a tabela abaixo sobre a correspondência entre milhas e quilômetros (note que 1 milha é igual 1,609 quilômetros) ate 10:
Milhas                        Quilômetros

1                                  1,609
2                                  3,218
...
'''
print('milhas ------ quilometros')
for m in range(1, 11):
    km = m * 1.609
    print(f'{m}                {km}') 