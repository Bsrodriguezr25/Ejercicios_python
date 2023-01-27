#Hacer un Programa en PYTHON   para una empresa trabajan n empleados cuyos sueldos oscilan entre $600000 y $1000000 Realizar un programa que informe de cuantos empleados cobran menos de 700000 y cuantos más de 900000. Informar también del total que gasta la empresa en pagar a sus empleados.

n = int (input("Cuantos empleados son ?"))
x = 0
menor = 0
mayor= 0
coste= 0
sueldo=0
for x in range (n):
  sueldo = float (input("Ingres el sueldo: "))
if (sueldo >=600000 and sueldo<700000):
  menor = menor + 1
elif (sueldo>900000 and sueldo <=1000000):
  mayor = mayor+ 1
  coste = coste + sueldo
#x = x + 1
print (f"Cantidad de emepleados con sueldo menor {menor}")
print (f"Cantidad de emepleados con sueldo mayor {mayor}")
print (f"Total pagado a los empleados {coste}")