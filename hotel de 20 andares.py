for int in range (1, 20):
     if(int == 13):
          continue
else:
     print(int)
     contador = 1
     while(contador <= 20):
          if(contador == 13):
               contador = contador + 1
               continue
          else:
               print(contador)
               contador = contador + 1
               for int in range(20, 0, -1):
                    if(int == 13):
                         continue
                    else:
                         print(int)
