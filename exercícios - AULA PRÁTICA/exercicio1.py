'''
quando o exercicio pedir p fazer uma funcao, é pra fazer so o def e nao o programa inteiro
calculo de área

maneira mais economica:

def calc_area(base, altura):
    return(base*altura)/2
'''


def calc_area(base, altura):
    area = (base*altura)/2
    return area


a = int(input('informe a altura: '))
b = int(input('informe a base: '))
area = calc_area(a, b)
print(area)

'''
outro jeito chamando a funcao direto no print:

def calc_area(base, altura): 
      return altura
      
      
a = int(input('informe a altura: '))
b = int(input('informe a base: '))
print(calc_area(20,30))
'''