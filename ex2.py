lados = int(input('informe a quantidade de lados: '))

if lados == 3:
    print('é um triângulo')
elif lados == 4:
    print('quadrado')
elif lados == 5:
    print('pentágono')
elif lados == 6:
    print('hexágono')
elif lados == 7:
    print("Heptagono")
elif lados == 8:
    print("Octógono")
elif lados == 9:
    print("Eneágono")
elif lados == 10:
    print("Decágono")
else:
    print("valor inválido!")

#nao preciso colocar o else obrigatoriamente quando uso o elif