def calculadora (num1, num2, operacao):
     if (operacao == 1):
          return num1 + num2
     elif (operacao == 2):
          return num1 - num2
     elif (operacao == 3):
          return num1 * num2
     elif (operacao == 4):
          return num1 / num2
     else:
          return 0
     
executar = True

while (executar == True):
          print("Qual operação você quer realizar?")
          print("1: Soma  2: Subtração  3: Multiplicação  4: Divisão  0: Sair")
          operacao = int (input())
          if(operacao < 0) or (operacao > 4):
               print("Essa operação não existe")
          elif(operacao == 0):
               executar == False
          else:
               print("Insira o primeiro número:")
               num1 = int (input())
               print('Insira o segundo número')
               num2 = int (input())
               resultado = calculadora (num1, num2, operacao)
               print("O resultado da sua operação é:", resultado)