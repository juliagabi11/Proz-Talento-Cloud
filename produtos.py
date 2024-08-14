
def lista_produtos():
    lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores']
    return lista_produtos

lista_produtos = lista_produtos() 

for i in range(len(lista_produtos)):
  print(lista_produtos[i])



for i in range(len(lista_produtos)):
  print('Temos ' + lista_produtos[i] + ' à venda!')