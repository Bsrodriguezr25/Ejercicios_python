
#Desarrolle un programa en Python que almacenen   en una lista los días laborales de la semana, también que permita almacenar las horas que se trabaja en cada día laboral, el programa debe imprimir los días laborales juntos con la cantidad de horas trabajadas.


lista = []
horas = int(input("ingrese cuantos dias laboro: "))
n = 1

for i in range(horas):
  num = input(f"horas laboradas en el dia {n}: ")
  lista.append(int(num))
  n+=1

tupla = ("lunes","martes","miercoles","jueves","viernes")

for tupla in zip(lista, tupla): 
	print(tupla[1], "laboro",tupla[0], "horas")
"""
"""
dias = ("Lunes", "martes","miercoles", "jueves","viernes")
horas= []

for x in range (len(dias)):
  hora= input(f"ingrese la hora para el dia {dias[x]}")
  horas.append(hora)

for x in range(len(dias)):

 print(f"dia {dias[x]} , son : {horas[x]} horas")
