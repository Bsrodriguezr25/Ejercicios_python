#Escriba un programa que permita a un usuario escribir números en una lista. Una vez el usuario presiona la tecla Q el programa debe mostrar cuantos ceros  fueron ingresados por el usuario.

print(" Q para salir del programa ")
valores = []
numeroscero=0
entrada = input ("Ingrese el dato:")

while entrada != "Q":
  valores.append(int (entrada))
  entrada = input("Ingrese el dato:")

for numero in valores:
  
  if numero==0:
    numeroscero+=1

print("cantidad de ceros son : ", numeroscero)