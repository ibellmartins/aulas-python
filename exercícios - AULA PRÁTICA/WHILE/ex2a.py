vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'
azul = '\033[34m'
branco = '\033[37m'

opcao = 0
while opcao != 5:
     print(branco, "\n Mack cores")
     print("1-vermelho")
     print("2-azul")
     print("3-verde")
     print("4-amarelo")
     print("5-branco")
     opcao = int(input("informe sua opção: "))

     if opcao == 1:
         print(vermelho, "MACKENZIE")
     elif opcao == 2:
         print(azul, "MACKENZIE")
     elif opcao == 3:
         print(verde, "MACKENZIE")
     elif opcao == 4:
         print(amarelo, "MACKENZIE")
     elif opcao == 5:
         print("acabou")
     else: 
          print("opção inválida!")
