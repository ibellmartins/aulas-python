def pizza(p, f, c): #posso passar parametros com nomes diferentes das variaveis, o q importa é a POSICAO! 
    return int((p * f)/c) #esse int é p retorno ser inteiro, se retirá-lo, o resultado final é dado em float por default

qtd_pizza = int(input("quantas pizzas? "))
qtd_fatias = int(input("quantas fatias terá em cada pizza? "))
qtd_conv = int(input("quantos covidados terá? "))
print(f'a quantidade de fatias que cada um poderá comer será {pizza(qtd_pizza, qtd_fatias, qtd_conv)}') #aqui eu coloco os nomes das variaveis