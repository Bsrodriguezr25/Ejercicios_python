#print ("hola mundo")

'''robot = ["bipedo","6",["caminar","correr","saltar"]]
print (robot[2][1])'''

# sirve para actualizar algun dato de la lista
'''robot = ["bipedo","6",["caminar","correr","saltar"]]
robot [2][1] = "trotar"
print (robot)'''

#es un tipo de tupla la cual no va con "[]" si no que va con "()" a diferencia de las listas
'''xy = ("primavera","verano","otono","invierno")
print (xy[0])'''

#esto es un diccionario donde se pueden realizar consultas de las claves y cambiar los valores
'''dic = {'clave1': "bipedo",
        'clave2': 6,
        'clave3': ["caminar","correr","saltar"]
}

dic2 = dic["clave3"][1]
print (dic2)'''

#instrucciones de decision logica

libros = int (input('cuantos libros lees anualmente: '))

if libros > 15:
    print ("eres un buen lector")

else:
    print ("Necesitas leer mas")


