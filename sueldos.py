"""
escriba un programa que dado como dato la categoria y el sueldo de un trabajador, calcule el aumento correspondiente.
"""
# se solicita el sueldo del trabajador
sueldo = float(input("ingrese el sueldo: "))
print("su sueldo actual es de: ", sueldo )
# se solicita la categoria del trabajador
categ = int(input("ingrese su categoria: "))
print("su categoria es: ", categ)

# se realiza el proceso de ejecucion
if(categ == 1):
  total = (sueldo * 0.15)
  print("su aumento es de: ", total)
  total1 = (sueldo + total)
  print("su nuevo sueldo es de: ", total1)
elif(categ == 2):
  total = (sueldo * 0.10)
  print("su aumento es de: ", total)
  total1 = (sueldo + total)
  print("su nuevo sueldo es de: ", total1)
elif(categ == 3):
  total = (sueldo * 0.08)
  print("su aumento es de: ", total)
  total1 = (sueldo + total)
  print("su nuevo sueldo es de: ", total1)
elif(categ == 4):
  total = (sueldo * 0.07)
  print("su aumento es de: ", total)
  total1 = (sueldo + total)
  print("su nuevo sueldo es de: ", total1)
else:
  print("ingreso datos erroneos intente nuevamente")