#verifica se o numero é par ou ímpar
def num(a):
    if a % 2 == 0:
        return True
    else:
        return False


a = int(input("digite um numero: "))
result = num(a)
if result:
    print("o numero é par!")
else:
    print("o numero é ímpar!")