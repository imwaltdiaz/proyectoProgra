import time
import random
def editarEncuesta():
  tipoDeEncuesta = str(input("Seleccione tipo de encuesta a editar BAWR - CSAT - PSUR: "))
  preguntaNueva = str(input("Ingrese nueva pregunta: "))
  dificultad = int(input("Ingrese dificultad (1 Menor - 5 Mayor): "))
  idAsignado = random.randint(10000,20000)
  orden = int(input("Orden ascendende: 1\nOrden descendente 2:\n Orden: "))
  if orden == 1:
    sort(orden)
  elif orden == 2:
    sort(orden)
def resolverEncuesta():
  pass
def verResultados():
  pass
def sort(orden):
  pass
def main():
  nombre = str(input("Ingrese su nombre: "))
  codigoCliente = int(input("Ingrese su codigo: "))
  opcion = str(input("Opcion 1: Editar encuesta\nOpcion 2: Resolver encuesta\nOpcion 3: Ver resultados\nOpcion: "))
  if opcion == 1:
    editarEncuesta()
  elif opcion == 2:
    resolverEncuesta()
  elif opcion == 3:
    verResultados()


main()
