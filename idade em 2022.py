print ("Digite seu nome:") 
nome = input ()

executar = True

while (executar == True):
     print ("Ano de nascimento:")
     try:
          ano = int(input())
          if(ano < 1922) or (ano > 2021):
               print("Necessário ser entre 1922 e 2021")
          else:
               idade = 2022 - ano
               print("Você", nome, "completou ou completará", idade, "anos de idade em 2022")
               executar = False
     except:
          print("Anos permitido apenas escrito em números")
     