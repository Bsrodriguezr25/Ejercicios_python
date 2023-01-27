#Hacer un Programa en PYTHON  que pida un numero entero del 1 al 10. Mostrar después la tabla de multiplicar de dicho número.

num=int(input("Ingrese un numero: "))
for x in range(1,11):
    tabla=num*x
    print(f"{num} * {x} = {tabla}")