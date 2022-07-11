import json
import time
import random
def editarEncuesta(nombre, codigoCliente):
  tipoDeEncuesta = str(input("\nSeleccione tipo de encuesta a editar BAWR - CSAT - PSUR: "))
  preguntaNueva = str(input("\nIngrese nueva pregunta: "))
  dificultad = int(input("\nIngrese dificultad (1 Menor - 5 Mayor): "))
  
  if tipoDeEncuesta == "csat" or "CSAT":
    listObj = []
    # Cambiar test.json por csat.json
    with open("test.json", encoding = "utf-8") as fp:
      listObj = json.load(fp)
    listObj.append({
      "question": preguntaNueva,
      "answers": {
        "a": "si",
        "b": "no"
      },
      "level": dificultad
    })
    with open("test.json", 'w', encoding = "utf-8") as json_file:
      json.dump(listObj, json_file, 
                        indent=2,  
                        separators=(',',':'))

    print("Su pregunta ha sido agregada correctamente")
  elif tipoDeEncuesta == "bawr" or "BAWR":
    listObj = []
    # Cambiar test.json por csat.json
    with open("test.json", encoding = "utf-8") as fp:
      listObj = json.load(fp)
    listObj.append({
      "question": preguntaNueva,
      "answers": {
        "a": "si",
        "b": "no"
      },
      "level": dificultad
    })
    with open("test.json", 'w', encoding = "utf-8") as json_file:
      json.dump(listObj, json_file, 
                        indent=2,  
                        separators=(',',':'))
    # encuestaOrdenada
    print("Su pregunta ha sido agregada correctamente")
  elif tipoDeEncuesta == "psur" or "PSUR":
    listObj = []
    # Cambiar test.json por csat.json
    with open("test.json", encoding = "utf-8") as fp:
      listObj = json.load(fp)
    listObj.append({
      "question": preguntaNueva,
      "answers": {
        "a": "si",
        "b": "no"
      },
      "level": dificultad
    })
    with open("test.json", 'w', encoding = "utf-8") as json_file:
      json.dump(listObj, json_file, 
                        indent=2,  
                        separators=(',',':'))
    # encuestaOrdenada
    print("Su pregunta ha sido agregada correctamente")
  else: 
    print("Ingrese una opción válida por favor")
    editarEncuesta(nombre,codigoCliente)

def resolverEncuesta(nombre,codigoCliente):
  tipoDeEncuesta = str(input("Seleccione tipo de encuesta a editar BAWR - CSAT - PSUR: "))
  n = int(input("Ingrese numero de encuestas de este tipo a resolver"))
  #orden = int(input("Orden ascendende: 1\nOrden descendente 2:\n Dificultad en orden: "))
  # sort(orden, lista ,nombre)
  idAsignado = random.randint(10000,20000)
  print("se le ha asignado el id: ", idAsignado)
  # Resolver encuesta
  if tipoDeEncuesta == "csat" or "CSAT":
    
  elif tipoDeEncuesta == "bawr" or "BAWR":
    
  elif tipoDeEncuesta == "psur" or "PSUR":
   
  else: 
    print("Ingrese una opción válida por favor")
    editarEncuesta(nombre,codigoCliente)
  for i in range (0,n):
    
  
  
def verResultados():
   f = open("results.json")
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
  codigoCliente = int(input("\nIngrese su codigo: "))
  opcion = int(input("\nOpcion 1: Editar encuesta\nOpcion 2: Resolver encuesta\nOpcion 3: Ver resultados\n\nOpcion: "))
  if opcion == 1:
    editarEncuesta(nombre,codigoCliente)
  elif opcion == 2:
    resolverEncuesta(nombre,codigoCliente)
  elif opcion == 3:
    verResultados()
main()
