#Hacer un Programa en PYTHON que calcule la media de una cantidad de números introducidos por teclado, la cantidad de números la indica el usuario.

n = float(input("ingrese la cantidad de numeros a promediar: "))

suma = 0
i = 1

while(i<=n):
  print("ingrese el numero",i)
  numero = (float(input()))
  suma = suma+numero
  i+=1
prom=suma/n
print("la suma es: ",suma)
print("la media de los valores es de: ", prom)