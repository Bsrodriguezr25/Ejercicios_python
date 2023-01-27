"""
Una empresa tiene n empleados, usted ha sido contratado para realizar el diseño de un programa en python, que tenga en cuenta las siguientes consideraciones para calcular el sueldo de un obrero:
• Si trabaja 40 horas o menos se le paga $16.000 por hora trabajada.
• Si trabaja más de 40 horas se le paga $16.000 por cada una de las primeras 40 horas trabajadas y $20.000 por cada hora extra.
CONSIDERACIONES
SALARIO MENSUAL POR HORA $ 16.000
SALARIO HORA EXTRA $ 20.000
Horas normales de trabajo 40, si excede esta cantidad las horas se consideran como horas extras
"""

empleado = str(input("ingrese el nombre del empleado:  "))
print("el nobre del empleado es: ", empleado)

horas = int(input("ingrese las horas laboradas"))

if(horas <= 40):
  cal = horas
  total = (cal*16000)
  print("el sueldo es:", total)

elif(horas > 40):
  cal = horas
  fin = (cal - 40)
  total = ((cal- fin)*16000) + (fin*20000)
  print("el sueldo con horas extra es de: ", total)

num = float(input("ingrese un numero: "))
print ("el numero es", num)
