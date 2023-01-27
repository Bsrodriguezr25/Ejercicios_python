pregunta = str(input('trabajas desde casa: '))
tiempo = 0

if pregunta == True:
    print("eres afortunado")

if pregunta == False:
    print("trabajas fuera de casa")

    tiempo == int(input('cuanto tiempo haces al trabajo'))
    if tiempo == 0:
        print("trabajas desde casa")
    
    elif tiempo <= 20:
        print("es poco timepo")
    elif tiempo >= 21 and tiempo <= 45:
        print("es un tiempo razolnable")
    else:
        print("debes buscar otras rutas")

