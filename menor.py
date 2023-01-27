#Desarrolle un programa en python que permita leer tres valores y almacenarlos en las variables numero1,numero2, y numero3 respectivamente. El programa debe indicar cuál es el menor. Asumiendo que los tres valores introducidos por el teclado son valores distintos.

numero1 = float(input("ingrese el valor del primer numero: "))
numero2 = float(input("ingrese el valor del segundo numero: ")) 
numero3 = float(input("ingrese el valor del tercer numero: ")) 

if(numero1 < numero2) and (numero1 < numero3):
  print(f"numero menor {numero1}" )

elif(numero2 < numero1) and (numero2 < numero3):
  print(f"numero menor {numero2}" )
  
else:
  print(f"numero menor {numero3}")

  