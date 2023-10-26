somaNum = 0
qntNum = 0

num = int(input("digite um numero: "))
while num != 0:
    somaNum = somaNum + num
    qntNum = qntNum + 1
    num = int(input("digite um numero: "))

if qntNum == 0:
    media = 0
else:
     media = somaNum/qntNum
print(f"A média dos números é: {media}")
