#un almacen ofrece un descuento del 15% sobre el total de la compra, se desea saber cuanto pagara el cliente por total de la misma.

#pedimos el valor de la compra
valor_compra=float(input("ingrese el valor de la compra: "))
#calculamos el descuento
descuento = valor_compra*0.15
#calculamos el total a pagar
total = valor_compra-descuento
#imprimimos el resultado
print(f"el valor de la compra es: {valor_compra} el descuento es: {descuento} el total a pagar es: {total}")
