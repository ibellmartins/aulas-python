letra = input("Digite uma letra: ")
letra = letra.upper()  #considera letras maiusculas e minusculas
if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
    print('é uma vogal')
else:
    print('é uma consoante!')
