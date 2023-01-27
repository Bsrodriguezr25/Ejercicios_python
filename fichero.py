fichero = open('text.txt')
# print(fichero.read())

# print(fichero.readline())
# print(fichero.readline())

"""
caracter = fichero.readline(1)

while caracter !="":
  print(caracter)

  caracter = fichero.readline(1)
"""

# lineas = fichero.readlines()
# print(lineas)

lineas = fichero.readlines()

for linea in lineas:
  print(linea)