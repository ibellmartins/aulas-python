from random import *
secreto = randint(0, 100)
print(secreto)
tentativas = 0

while True:
    chute = int(input("digite um numero:"))
    tentativas += 1
    if chute == secreto:
        print(f"parabens, vc acertou em {tentativas}!")
        break
    elif chute < secreto:
        print("o valor é menor que o secreto")
    else:
        print("o valor é maior que o secreto")
        
    
