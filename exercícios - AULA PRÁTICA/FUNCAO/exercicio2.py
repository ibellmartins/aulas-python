def impar_par():
    if n % 2 == 0:
        return True
    else:
        return False
    

n = int(input("digite um numero inteiro: "))
if impar_par():
    print('esse numero é par!')
else: 
    print('esse numero é impar!')



'''
outra forma: 
def validacao(n):
    if n % 2 == 0: 
        return True
    else: 
        return False
    

n = int(input('digite um numero inteiro: '))
if validacao(n) == True:
    print('esse numero é par')
else:
    print('esse numero é ímpar.')
'''
