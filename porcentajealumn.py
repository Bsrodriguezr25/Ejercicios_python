""" El coordinador del Área desea saber qué porcentaje de hombres y que porcentaje de mujeres están cursando este semestre el curso de algoritmos, se conoce la cantidad de hombres y la cantidad de mujeres. """


mujer=float(input("ingrese la cantidad de mujeres: "))
hombre=float(input("ingrese la cantidad de hombres: "))

total= mujer+hombre

f = total*(mujer/100)
m = total*(hombre/100)

print("el porcentaje de mujeres del curso es:", int(f),"%")
print("el porcentaje de mujeres del curso es:", int(m),"%")