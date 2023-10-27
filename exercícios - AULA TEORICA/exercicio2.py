respostas = []

def print_relatorio():  #mostra a tabela
    print('Sistema Operacional\t Votos\t %')
    print('-'*40)
    print(f'windows\t \t {qtd_votos(1)}\t \t {porcent_SO(1)}') #qtd_votos(1) nao pega o valor do indice!! senao teria que inicializar em 0. ele pega a quantidade de numeros 1 que o usuario inputou
    print(f'linux\t \t {qtd_votos(2)}\t \t {porcent_SO(2)}')
    print(f'iOS\t \t {qtd_votos(3)}\t \t {porcent_SO(3)}')
    print(f'android\t \t {qtd_votos(4)}\t \t {porcent_SO(4)}')
    print(f'macOS\t \t {qtd_votos(5)}\t \t {porcent_SO(5)}')
    print('-'*40)
    print(f'Total: \t \t \t {len(respostas)}')


def qtd_votos(i):
    cont = 0
    for item in respostas:
        if item == i:
            cont+=1
    return cont


def porcent_SO(i):
    return math.trunc(respostas.count(i)*100 / len(respostas))


def mais_votados():
    pass


#bloco principal
while True:  #validacao
    r = int(input("qual Sistema Operacional vc mais usa?\n"
                  "1 - windows\n"
                  "2 - linux\n"
                  "3 - iOS\n"
                  "4 - android\n"
                  "5 - mac OS\n"
                  "Digite um numero ou 0 para sair"
                  ))
    if r == 0:
        break
    if r < 1 or r > 5:
        print('digite uma opcao valida pfv afff\n')
        continue #ignora as condicoes abaixo e volta - é a mesma coisa que um RETURN em uma função
    respostas.append(r)

print_relatorio()
mais_votados()
