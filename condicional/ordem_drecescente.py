preco_1 = (input('Digite o primeiro valor: '))
preco_2 = (input('Digite o segundo valor: '))
preco_3 = (input('Digite o terceiro valor: '))

if (preco_1 > preco_2) and (preco_1 > preco_3):
  if (preco_2 > preco_3):
    print(preco_1, preco_2, preco_3)
  else:
    print(preco_1, preco_3, preco_2)
if (preco_2 > preco_1) and (preco_2 > preco_3):
  if (preco_1 > preco_3):
    print(preco_2, preco_1, preco_3)
  else:
    print(preco_2, preco_3, preco_3)
if (preco_3 > preco_1) and (preco_3 > preco_2):
  if (preco_1 > preco_2):
    print(preco_3, preco_1, preco_2)
  else:
    print(preco_3, preco_2, preco_1)