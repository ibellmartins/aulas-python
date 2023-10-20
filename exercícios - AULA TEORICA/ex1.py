num = []
soma = 0

while True:
    n = int(input('Digite um numero e zero para parar: '))
    if n == 0:
        break
    num.append(n)
    soma+=n

media = soma/len(num)
print(f'{media:.2f}')
print(num)