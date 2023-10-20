
def exibeMsg():
    print('O programa faz a conversao de Celsius para Fahrenheit e vice-versa.')
    print('Informe o tipo de conversao e a faixa de temperatura')


def verificaOpcao():
    print('\nDigite <F> para converter de Fahrenheit para Celsius ')
    print('\nDigite <C> para converter de Celsius para Fahrenheit ')
    while True:    #isso é uma tecnica, sempre validaremos dados dessa forma
        escala = input().upper()
        if escala == "F" or escala == "C":
            break
        else:
            print('Escala inválida. Digite novamente: ')
    return escala


def verificaIntervalo():
#validação dos dados,

exibeMsg()
escala = verificaOpcao()
