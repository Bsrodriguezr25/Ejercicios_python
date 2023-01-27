
#Hacer un Programa en PYTHON que pida por teclado dos números, muestre la suma de ellos en pantalla y pregunte al usuario si quiere realizar otra suma, en caso de ser si continúa haciendo sumas, en caso de ser no termina el proceso.

numero = True

while(numero):

 numero1 = int(input("ingrese primer numero: "))
 numero2 = int(input("ingrese segundo numero: "))

 suma = numero1 + numero2
 print(f"el resultado de la suma es: {suma}")
 mensaje = input("desea realizar otra suma: ")
 if (mensaje== "no"):
  numero = False
  break