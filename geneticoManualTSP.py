import random
import csv

ciudades = ['A', 'B', 'C', 'D', 'E']

mat_costos = []
with open('viajero.csv') as archivo:
  lector = csv.reader(archivo, delimiter=';')
  next(lector) 
  for fila in lector:
    mat_costos.append([int(x) for x in fila[1:]])

poblacion_tamaño = 15
generaciones = 15
prob_mutacion = 0.2

def generar_ruta():
  ruta = random.sample(ciudades[1:], len(ciudades) - 1)
  ruta.insert(0, 'A')
  return ruta

def aptitud(ruta):
  distancia = 0
  for i in range(len(ruta)):
    inicio = ruta[i]
    final = ruta[(i+1) % len(ruta)]
    distancia += mat_costos[ciudades.index(inicio)][ciudades.index(final)]
  return distancia
  
  
def seleccionar_padres(poblacion, aptitudes):
  return random.choices(
    population=poblacion, 
    weights=aptitudes, 
    k=int(len(poblacion)/2)
  )


def cruzar(padre1, padre2):
  hijo = padre1[:int(len(padre1)/2)] 
  for i in range(int(len(padre1)/2), len(padre1)):
    gen = padre2[i]
    if gen in hijo:
      indice = i 
      reemplazo = padre1[indice]
      while reemplazo in hijo:
        reemplazo = padre2[indice]
        indice = padre1.index(reemplazo)
      gen = reemplazo
    hijo.append(gen)
  
  return hijo

def mutar(individuo):
  ruta_mutada = individuo[:]  
  i = random.randint(1, len(ruta_mutada) - 1)
  j = random.randint(1, len(ruta_mutada) - 1)
  aux = ruta_mutada[i]
  ruta_mutada[i] = ruta_mutada[j]
  ruta_mutada[j] = aux

  return ruta_mutada 

poblacion = [generar_ruta() for _ in range(poblacion_tamaño)] 
for gen in range(generaciones):

  aptitudes = [aptitud(r) for r in poblacion]
  max_peso = max(aptitudes)
  pesos_invertidos = [(max_peso - peso)+10 for peso in aptitudes]
  
  padres = seleccionar_padres(poblacion, pesos_invertidos)
  
  hijos = []
  
  for i in range(0, len(padres), 1):
    if i+1<len(padres):
      hijo = cruzar(padres[i], padres[i+1]) 
      hijos.append(hijo)
    else:
      hijo = cruzar(padres[i], padres[0]) 
      hijos.append(hijo)


  for i in range(len(hijos)):
    if random.random() < prob_mutacion:
      hijos[i] = mutar(hijos[i]) 
  print("generacion",gen)  
  for i in range(len(poblacion)):

    print(f"{poblacion[i]} costo: {aptitudes[i]}")    
  total= sum(aptitudes)
  print("total ", total)
  
  poblacion = padres+hijos
  














