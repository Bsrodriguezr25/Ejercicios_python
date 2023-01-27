
#Hacer un Programa en PYTHON  donde Se ingresan un conjunto de n alturas de personas por teclado. El valor de la altura puede ser en metros o en centímetros(a elección de cada uno, lo comento para practicar con float). Mostrar el promedio de todas las alturas.

personas=int(input("Cuantas personas hay:"))
x=1
suma=0
while x<=personas:
    altura=float(input("Ingrese la altura: "))
    suma=suma+altura
    x=x+1
promedio=suma/personas
print("El promedio es ")
print(promedio)
