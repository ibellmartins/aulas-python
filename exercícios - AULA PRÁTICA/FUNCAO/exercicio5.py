def notas():
    media = (nota1 + nota2) / 2
    if media >= 7:
        return True
    else: 
        return False

while True:
    nota1 = float(input("digite sua nota 1: "))
    nota2 = float(input("digite sua nota 2: "))
    if nota1 >= 0 and nota1 <= 10 or nota2 >= 0 and nota2 <= 10:
        break
    else: 
        print("tente novamente.")

print(notas())