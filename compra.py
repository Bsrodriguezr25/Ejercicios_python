"""
Permita calcular el total a pagar por la compra de N camisas. Si se compran entre 1 a 4 camisas se aplica un descuento del 12.5%, si se compra una cantidad comprendida entre 5 y 8 camisas se aplica un descuento del 20% y si se compran cantidades mayores, se aplica un descuento del 31.5% sobre el total de la compra. Debe imprimirse en pantalla la compra final sin descuento, monto del descuento y la compra con descuento.
"""

cam = int(input("ingrese la catidad de camisas compradas: "))
val = 10000

if(cam <= 4):
  print(f"realizo la compra de {cam} camisetas")
  total = (val*cam)
  print("total compra", total)
  total2 = (total*0.125)
  print("descuento a realizar", total2)
  total3 = (total - total2)
  print("total a pagar es: ", total3)
elif(cam >= 5) and (cam <= 8):
  print(f"realizo la compra de {cam} camisetas")
  total = (val*cam)
  print("total compra", total)
  total2 = (total*0.2)
  print("descuento a realizar", total2)
  total3 = (total - total2)
  print("total a pagar es: ", total3)
elif(cam > 8):
  print(f"realizo la compra de {cam} camisetas")
  total = (val*cam)
  print("total compra", total)
  total2 = (total*0.315)
  print("descuento a realizar", total2)
  total3 = (total - total2)
  print("total a pagar es: ", total3)
else:
  print("ingrese un numero adecuado")