def media_sal():
    soma = 0
    for s in salarios:
        soma += s
    return soma/len(salarios)    #retorna media calculada


def maior_sal():
    maior = salarios[0] #inicializa com o primeiro salario
    for i in range(1, len(salarios)):
        if salarios[i] > maior:
            maior = salarios[i]
    print(f'O maior salário é R${maior}. ')


def contar_sal():
    menor = 0
    for i in salarios:
        if i < 850:
            menor += 1
    return menor



def exibe_sal():
    for i, s in enumerate(salarios):
        print(f'Salario {i+1}: R$ {s}')


salarios = []

for s in range(10):
    sal = float(input('digite seu salario: '))
    salarios.append(sal)

print('resultados:')
print(f'media dos salarios: R${media_sal()}') #esse pede pra dar um return na funcao, entao usamos o print
maior_sal()    #basta chamar a função, o print estará dentro dela
print(f'Salarios menores que R$850: {contar_sal()}')
exibe_sal()