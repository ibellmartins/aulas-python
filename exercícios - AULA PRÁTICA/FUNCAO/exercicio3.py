def nome_caps():
    return nome.upper()

def nome_low():
    return nome.lower()

nome = input("insira seu nome completo: ")
print(nome_caps())
print(nome_low())


# sem variaveis (mais economico e simples porem so posso fazer com um método)
def nome_caps():
    return input('digite seu nome: ').upper()

print(nome_caps())

