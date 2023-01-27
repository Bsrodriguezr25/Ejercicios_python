"""
un estudiante necesita calcular el valor del area de una figura geometrica disponibles son el triangulo, rectangunlo y un hexagono
"""

menu = """
Bienvenido a nuestro programa calcular areas
Cual area desea calcular?

1. triangulo
2. circulo
3.rectangulo
4. hexagono
"""

import math

print(menu)

opcion = int(input("ingrese la opcion deseada:  "))

if (opcion==1):
  print("ingreso la opcion triangulo-")
  base = float(input("ingrese la base: "))
  altura = float(input("ingrese la altura"))
  area=(base*altura)/2
  print(f"el area del triangulo es: {area}")
  
elif (opcion==2):
  print("ingreso la opcion circulo-")
  radio = float(input("ingrese el radio: "))
  area=(3.14*radio**2)
  print(f"el area del circulo es: {area}")
  
elif (opcion==3):
 print("ingreso la opcion rectangulo-")
 ancho = float(input("ingrese la base: "))
 largo = float(input("ingrese la altura"))
 area=(ancho*largo)
 print(f"el area del rectangulo es: {area}")
  
elif (opcion==4):
 print("ingreso la opcion hexagono-")
 lado = float(input("ingrese el tamano de un lado: "))
 perimetro = lado*6
 apotema = math.sqrt((lado*lado)-((lado/2)*(lado/2))) 
 area=(perimetro*apotema)/2
 print(f"el area del hexagono es: {area}")
else:
  print("la opcion no es correcta")
  