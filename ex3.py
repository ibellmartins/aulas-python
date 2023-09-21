mes = int(input("digite um mês qualquer: "))
dia = int(input("digite um dia qualquer: "))

if (mes == 9 and dia >= 21) or (mes == 10 or mes == 11) or (mes == 12 and dia <=20):
    print('é primavera!')
else:
    if (mes == 12 and dia >= 21) or (mes == 1 and mes == 2) or (mes == 3 and dia <= 19):
        print("é verão!")
    else:
        if (mes == 3 and dia >= 20) or (mes == 4 and mes == 5) or (mes == 6 and dia <= 20):
            print("é outono!")
        else:
            print("é inverno!")