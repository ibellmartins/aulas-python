def exibeMsg():
    print('O programa faz a conversao de Celsius para Fahrenheit e vice-versa.')
    print('Informe o tipo de conversao e a faixa de temperatura')


def verificaOpcao():
    print('\nDigite <F> para converter de Fahrenheit para Celsius ')
    print('\nDigite <C> para converter de Celsius para Fahrenheit ')
    while True:   #validação 
        validar = input().upper()
        if validar == 'F' or validar == 'C':
            break
        else:
            print('valor inválido. Digite novamente:')
    return validar


def verificaIntervalo():
    while True: #validação
        inicio = int(input('digite o valor inicial: '))
        fim = int(input('digite o valor final: '))
        if fim > inicio: 
            return inicio, fim
        else: 
            print('o valor final deve ser maior que o inicial. ')


def exibeFahrenheitToCelsius(inicio, fim): 
    print('\nConversão de Fahrenheit para Celsius:')
    for f in range(inicio, fim): 
        c = (f - 32)/1.8
    print(f'Fahrenheit: {f:.2f} - Celsius: {c:.2f}')


def exibeCelsiusToFahrenheit(inicio, fim):
    print('\nConversão de Celsius para Fahrenheit: ')
    for c in range(inicio, fim):
        f = c * 1.8 + 32
    print(f'Celsius: {c:.2f} - Fahrenheit: {f:.2f}')


exibeMsg()
validar = verificaOpcao()
inicio, fim = verificaIntervalo()
if validar == 'F':
    exibeFahrenheitToCelsius(inicio, fim)
else:
    exibeCelsiusToFahrenheit(inicio, fim)
