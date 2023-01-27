"""
en caso de que sea rojo, el jugador obtendrá 10 puntos
en caso de que sea verde obtendrá 5 puntos 
y en el caso de que sea azul obtendrá solamente 2 puntos. 


Si el jugador derriba más de 10 rojos se le dará un bonus del 10% sobre el puntaje final, 
si derriba más de 5 verdes se le da un bonus del 5%, 
y para los azules si derribó más de 2 uno del 2%, 

tenga en cuenta que el valor del puntaje final debe mostrase de tipo entero, es decir si el resultado 32.78 debe mostrase 32. 

Diseñe un programa que le permita al usuario saber cuántos puntos en total ganó luego de una partida dependiendo del color de los alienígenas que haya derribado, y la cantidad.

 

Nota: Ten en cuenta que es un solo intento, el programa deberá (a través de consola) obtener el color y el número de naves que derribo. 

Por ejemplo:

Ingrese la cantidad de rojos derribados:  2

Ingrese la cantidad de verdes derribados: 5

Ingrese la cantidad de azules derribados: 12

Puntaje total: 70
  
"""

rojos = int(input("ingrese la cantidad de rojos derribados:  "))
verdes = int(input("ingrese la cantidad de verdes derribados:  "))
azules = int(input("ingrese la cantidad de azules derribados:  "))

puntajer = rojos * 10
puntajev = verdes * 5
puntajea = azules * 2

bonor = 0
bonov = 0
bonoa = 0

suma = puntajea + puntajer + puntajev


if(rojos > 10):
  
  bonor = suma * 0.10

if(verdes > 5):

  bonov = suma * 0.05

if(azules > 2):

  bonoa = suma * 0.02

total = int(suma + bonor + bonov + bonoa)

print("puntaje total: ", total)
