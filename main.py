import json
import time
import random
def editarEncuesta(nombre, codigoCliente):
  tipoDeEncuesta = str(input("Seleccione tipo de encuesta a editar BAWR - CSAT - PSUR: "))
  preguntaNueva = str(input("Ingrese nueva pregunta: "))
  dificultad = int(input("Ingrese dificultad (1 Menor - 5 Mayor): "))
  idAsignado = random.randint(10000,20000)
  orden = int(input("Orden ascendende: 1\nOrden descendente 2:\n Orden: "))
  encuestaOrdenada = sort(orden)
  

def resolverEncuesta(nombre,codigoCliente):
  tipoDeEncuesta = str(input("Seleccione tipo de encuesta a editar BAWR - CSAT - PSUR: "))
  n = int(input("Ingrese numero de encuestas de este tipo a resolver"))
  orden = int(input("Orden ascendende: 1\nOrden descendente 2:\n Dificultad en orden: "))
  sort(orden, lista ,nombre)
  idAsignado = random.randint(10000,20000)
  print("se le ha asignado el id: ", idAsignado)
  # Resolver encuesta
    
  resultados = json.dumps(results)
  f = open("dict.json","w")
  f.write(resultados)
  f.close()
def verResultados():
   f = open("resultados.json")
   data = json.load(f)
   n = int(input("1: Desea ver resultados de un cliente en especifico.\n2: Desea ver una encuesta en particular "))
   if n == 1:
    tipoDeEncuesta = str(input("Seleccione tipo de encuesta a buscar BAWR - CSAT - PSUR: "))
    codigoDeCliente = int(input("Ingrese codigo de cliente: "))
    idAsignado = int(input("Ingrese id: "))
    pass
   elif n == 2:
    nombre = str(input("Ingrese id de la encuesta"))
# Sort de emergencia:
def sort(orden, lista, nombre):
  if orden == 1:
    ascendente = sorted(lista[nombre], key=lambda x: (lista[nombre][x][id]))
    return ascendente
  elif orden == 2:
    descendente = sorted(lista[nombre], key=lambda x: (lista[nombre][x][id]), reverse=True)
    return descendente
  
# Sort con quicksort
def main():
  nombre = str(input("Ingrese su nombre: "))
  codigoCliente = int(input("Ingrese su codigo: "))
  opcion = int(input("Opcion 1: Editar encuesta\nOpcion 2: Resolver encuesta\nOpcion 3: Ver resultados\nOpcion: "))
  if opcion == 1:
    editarEncuesta(nombre,codigoCliente)
  elif opcion == 2:
    resolverEncuesta(nombre,codigoCliente)
  elif opcion == 3:
    verResultados()
main()
