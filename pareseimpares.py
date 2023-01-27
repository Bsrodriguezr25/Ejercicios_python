#Desarrollar un programa que permita cargar N NUMEROS ENTEROS Y LUEGO NOS INFORME CUANTOS valores fueron pares y cuantos impares. emplear operador % 

cantidad = int (input ("ingrese cantida de numeros: "))
x=0
pares = 0
impares =0

while(x<cantidad):
  numero = int (input ("ingrese un numero"))
  if(numero % 2==0):
    print("es par")
    pares+=1
  else:
    print("impar")
    impares +=1
  x+=1
print(f"Total de pares {pares}")
print(f"Total de impares {impares}")