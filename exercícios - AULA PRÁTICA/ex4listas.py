'''
4 - Foram anotadas as idades e alturas de 10 alunos (os dados foram armazenados em listas distintas).
Faça um programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
'''

idades = []
alturas = []
soma = 0

for i in range(10):
    idade = int(input(f'informe a idade do aluno {i+1}:'))
    alt = float(input(f'informe a altura do aluno {i+1}: '))
    idades.append(idade) #append: adiciona itens no fim da lista conforme o usuario for inputando
    alturas.append(alt)
    soma = soma + alt

media = soma/10
for i in range(10): #esse for significa que vou olhar um elemento um por um
    if idades[i] > 13: #se e somente se a idade for maior que 13, me interessa olhar a altura
        if alturas[i] < media:
            cont = cont + 1

print(f'O numero de alunos abaixo da media é: {cont}')
print(idades)
print(alturas)