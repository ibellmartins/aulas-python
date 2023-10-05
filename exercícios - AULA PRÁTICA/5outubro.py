maximo = 5
cont = 0
avaliaOtimo = 0
avaliaPessimo = 0
idadeTotal = 0
maioridadeBom = 0
for num in range(1, 100):
    print(f"Pessoa {num}: ")
    while True:
     idade = int(input("digite sua idade: ")) 
     if idade <= 14:
         print("Idade inválida!!!")
     else:
         break
    idadeTotal += idade
    cont += 1
    print("A - Otimo\n B - Bom\n C - Regular\n D - Ruim\n E - Péssimo ")
    avaliacao = input("digite sua avalição: ").upper()
    if avaliacao == "A":
        avaliaOtimo += 1
    elif avaliacao == "B" and idade > maioridadeBom:
        maioridadeBom = idade
    elif avaliacao == "D":
        avaliaPessimo += 1

mediaIdade = idadeTotal / cont
percentPessimo = (avaliaPessimo / cont) * 100
print(f"A quantidade de respostas Ótimo foi {avaliaOtimo}")
print(f"A média da idades é {mediaIdade}")
print(f"A porcentagem de respostas Péssimo é {percentPessimo}")
print(f"A maior idade entre as pessoas que responderam Bom é {maioridadeBom}")