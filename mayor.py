
#Realice un programa que a partir de la edad de una persona verifique o diga si es mayor de edad o no.

edad = int(input("ingrese su edad: "))

if(edad < 18):
  print(f"usted tiene {edad} anos y es menor de edad")

elif(edad >= 18):
  print(f"usted tiene {edad} anos y es mayor de edad")

else:
  print("intente nuevamente")
  