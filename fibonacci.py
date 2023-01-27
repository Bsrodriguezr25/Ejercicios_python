#Seire fibonacci

anterior = 0
posterior = 1

tamano = int(input("el tamano de la serie es: "))
tamano -=2
print(anterior)
print(posterior)
for x in range(tamano):
  serie = anterior + posterior
  print(serie)
  anterior = posterior
  posterior = serie