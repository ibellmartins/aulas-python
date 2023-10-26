#2 - Faça um Programa que leia 10 caracteres, armazene-os em uma lista e apresente quantas consoantes foram lidas. Imprima as consoantes.


def contaConsoante(letras):
    cont = 0
    for z in letras:   #esse for é exclusivo para listas. o z é um elemento
        if z != "A" and z != "E" and z != "I" and z != "O" and z != "U":
            cont = cont + 1
            print(f'Consoante: {z}') #mostra todos as consoantes inputadas
    return cont


letras = []
for i in range(10):
    i = input("digite uma letra: ")
    i = i.upper() #padroniza a entrada
    letras.append(i)

total = contaConsoante(letras)
print(f'o total de consoantes é {total}')