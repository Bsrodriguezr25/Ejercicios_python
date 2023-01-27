"""
tupla = ("hola", 3.4, 3, True, "adios")

for i in range(len(tupla)):
  print(tupla[i])
"""
"""
diccionario = {
  "nombre":"carlos",
  "edad":25,
  "cedula":"1030677715"
}

print(diccionario["cedula"])
print(diccionario.keys())
print(diccionario.values())
"""
"""
diccionario = {
  "nombre":"stiven",
  "edad":25,
  "cedula":"1030677715"
}

print(diccionario["cedula"])
print(diccionario.keys())
print(diccionario.values())

for key in diccionario:
  print(key)

for key in diccionario:
  print(diccionario[key])

for key in diccionario:
  print(key,diccionario[key])
"""

"""
Hacer un programa en python utilizando diccionarios que permita hacer la traduccion de una palabra del español al ingles. las palabras a traducir son:
amarillo
azul
rojo
verde
rosado
blanco
negro
purpura
"""
"""
diccionario = {
  "amarillo":"yellow",
  "azul":"blue",
  "rojo":"red",
  "verde":"green",
  "rosado":"pink",
  "blanco":"white",
  "negro":"black",
  "purpura":"purple",
}
color = str(input("ingrese el color que desea traducir: "))

print("traduccion: ",diccionario[color])
"""

"""
Escriba un programa que pida dos listas al usuario y permita calcular la sumatoria de las dos listas 
"""

lista1 = []
lista2 = []
n = 1
m = 1
input("ingrese elementos de la primer lista: ")

while(n < 5):
  x = (input(f"lista uno {n}: "))
  lista1.append(x)
  n +=1
while(m < 5):
  x = (input(f"lista dos {n}: "))
  lista2.append(x)
  m +=1
  
print("la suma es: ", n + m)