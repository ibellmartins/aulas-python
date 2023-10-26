

def calcula(pizza, fatias, conv):
    return int((pizza * fatias)/conv)


pizza = int(input('insira a quantidade de pizzas: '))
fatias = int(input('insira a quantidade de pedacos que cada pizza terá: '))
conv = int(input('insira a quantidade de convidados: '))

qtd = calcula(pizza, fatias, conv)
print(f'cada convidado poderá comer {qtd} fatias.')