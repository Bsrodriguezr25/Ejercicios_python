#Escribir un Programa en PYTHON que solicite ingresar la nota de 5 alumnos, el programa debe informar de cuantos han aprobado y cuantos han perdido.

paso = 0
perdio = 0
num = 1

while(num <=5):
  nota = float(input(f"ingrese la nota final del alumno {num}:  "))
  num +=1
  if(nota>=3):
    paso += 1

else:
  perdio +=1

print(f"de los 5 alumnos, {paso} aprobaron y {perdio} perdieron")