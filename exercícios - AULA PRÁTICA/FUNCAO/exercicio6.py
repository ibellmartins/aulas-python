def validacao():
    n1 = int(input('digite um numero: '))
    n2 = int(input('digite outro numero: '))  
    while True: 
        if n2 > n1:
            break
        else:
            print('n2 deve ser maior que n1.')
    return n1

n1 = validacao()