#Un alumno desea saber cuál será su calificación en el primer corte en el curso de Python. Dicha calificación se compone de los siguientes porcentajes:
#55% del promedio de Quices
#30% el examen parcial
#15% el trabajo final 

#se solicita ingresar las notas
nota_uno=float(input("ingrese la nota de quices: "))
nota_dos=float(input("ingrese la nota del parcial: "))
nota_tres=float(input("ingrese la nota del trabajo final: "))

#calculamos el porcentaje
uno = nota_uno*0.55
dos = nota_dos*0.30
tres = nota_tres*0.15

#calculamos el total de las notas
total= uno+dos+tres

#imprimimos el resultado
print(f"la nota uno es: {uno} la nota dos es: {dos} la nota tres es: {tres} la nota total es {total}")