# 1 - Faça um Programa que leia 5 números inteiros, armazene-os em uma lista e mostre-os.


numeros = []

for n in range(5):
    n = int(input('digite um numero: '))
    numeros.append(n)

print(numeros)


#outro jeito de resolver usando o insert. lembrar que:
#insert: precisa dizer em qual indice vc quer acrescentar o item
#append: acrescenta valores no final da lista automaticamente

numeros = []

for n in range(5):
    n = int(input('digite um numero: '))
    numeros.insert(1,n)
print(numeros)