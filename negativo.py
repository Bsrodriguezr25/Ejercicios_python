#Hacer un Programa en PYTHON , que pida números mientras no se ingrese uno negativo. Al final, se debe mostrar la suma de los números ingresados

bandera = True
suma = float()

while (bandera):
  numero = float(input("ingrese el numero: "))

  if(numero >= 0):
    suma = suma + numero
  else:
    bandera = False

print (f"la suma es: {suma}")