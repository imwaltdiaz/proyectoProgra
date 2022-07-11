import json
import time
import random
def editarEncuesta(nombre, codigoCliente):
  tipoDeEncuesta = str(input("\nSeleccione tipo de encuesta a editar BAWR - CSAT - PSUR: "))
  preguntaNueva = str(input("\nIngrese nueva pregunta: "))
  dificultad = int(input("\nIngrese dificultad (1 Menor - 5 Mayor): "))
  # orden = int(input("\nOrden ascendende: 1\nOrden descendente 2:\n Orden: "))
  # encuestaOrdenada = sort(orden, )
  dicc = {}
  # terminar por añadir al json
  # crear diccionario igual al json 
  if tipoDeEncuesta == "csat" or "CSAT":
    # data = json.load('test.json')
    # data[preguntaNueva] = 'value'
    # json.dump('csat.json', data)
    # with open("csat.json", "r+") as f:
    #   data = json.load(f.read())
    #   data[preguntaNueva] = "bang"
    
    #f = open("csat.json","a")
    #dicc.setdefault("pregunta",preguntaNueva)
    #dicc.setdefault("dificultad",dificultad)
    #f.write(dicc)
    # encuestaOrdenada
    print("Su pregunta ha sido agregada correctamente")
  elif tipoDeEncuesta == "bawr" or "BAWR":
    f = open("bawr.json","a")
    dicc.setdefault("pregunta",preguntaNueva)
    dicc.setdefault("dificultad",dificultad)
    f.write(dicc)
    # encuestaOrdenada
    print("Su pregunta ha sido agregada correctamente")
  elif tipoDeEncuesta == "psur" or "PSUR":
    f = open("psur.json","a")
    dicc.setdefault("pregunta",preguntaNueva)
    dicc.setdefault("dificultad",dificultad)
    f.write(dicc)
    # encuestaOrdenada
    print("Su pregunta ha sido agregada correctamente")
  else: 
    print("Ingrese una opción válida por favor")
    editarEncuesta(nombre,codigoCliente)

def resolverEncuesta(nombre,codigoCliente):
  respcsat = []
  respbawr = []
  resppsur = []
  csat = open("csat.json", "r")
  bawr = open("bawr.json", "r")
  psur = open("psur.json", "r")
  tipoDeEncuesta = str(input("Seleccione tipo de encuesta a editar BAWR - CSAT - PSUR: "))
  n = int(input("Ingrese numero de encuestas de este tipo a resolver: "))
  #orden = int(input("Orden ascendende: 1\nOrden descendente 2:\n Dificultad en orden: "))
  #sort(orden, lista ,nombre)
  idAsignado = random.randint(10000,20000)
  print("se le ha asignado el id: ", idAsignado)
  for i in range(n):  
      if tipoDeEncuesta == "CSAT" or "csat":
        print("\nSeleccionaste la encuesta CSAT\n")
        for linea in csat:
            linea = linea.strip()
            palabras = linea.split(",")
            for i in range(0, len(palabras)):
                print(palabras[i])
            for j in range(0, 1):
                resp = str(input("\nIngresa tu respuesta: "))
                respcsat.append(resp)
        print("Gracias por responder")
        return respcsat
        csat.close()
      elif tipoDeEncuesta == "BAWR" or "bawr":
          print("\nSeleccionaste la encuesta BAWR\n")
          for linea in bawr:
              linea = linea.strip()
              palabras = linea.split(",")
              for i in range(0, len(palabras)):
                  print(palabras[i])
              for j in range(0, 1):
                    resp = str(input("\nIngresa tu respuesta:\n"))
                    respbawr.append(resp)
          print("Gracias por responder")
          csat.close()
      elif tipoDeEncuesta == "PSUR" or "psur":
          print("\nSeleccionaste la encuesta PSUR\n")
          for linea in psur:
              linea = linea.strip()
              palabras = linea.split(",")
              for i in range(0, len(palabras)):
                  print(palabras[i])
              for j in range(0, 1):
                  resp = str(input("\nIngresa tu respuesta: "))
                  resppsur.append(resp)
          print("Gracias por responder")
          csat.close() 
  # Mostrar las preguntas 
  #with open('sample.json', 'r') as openfile:
    # Reading from json file
    #jsonDict = json.load(openfile)
    #for i in jsonDict[tipoDeEncuesta]:
      #for key, value in mydic.iteritems():
        #print (key, value)
  #Lo de abajo es para guardar resultados
  #resultados = json.dumps(results)
  #f = open("dict.json","w")
  #f.write(resultados)
  #f.close()

  
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
