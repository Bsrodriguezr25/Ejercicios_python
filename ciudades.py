
#crea una lista con 8 elementos cualquiera, ingresados por teclado y luego pedir al usuario la posicion del elemento que desea mostrar en la lista


lista = []
n = 1
input("ingrese 8 elementos")

while(n < 9):
  x = (input(f"elemento numero {n}: "))
  lista.append(x)
  n +=1

i = int(input("selecciones de 0 a 7 el elemento que quiere mostrar"))
print(lista[i])



ciudades= []

numero= int (input ("Ingrese la cantidad de ciudad es "))

for i in range (numero):
  ciudad= input ("Ingrese la ciudad: ")
  ciudades.append(ciudad)
  ciudades.sort()
for i in range (numero):
  print(ciudades[i])

elemento= int (input("Ingrese la posicion: "))
print(ciudades[elemento])