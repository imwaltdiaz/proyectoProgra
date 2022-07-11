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
  # falta preguntar por repetir n veces la encuesta
  idAsignado = random.randint(10000,20000)
  print("se le ha asignado el id: ", idAsignado)
  # Resolver encuesta
  if tipoDeEncuesta == "csat" or "CSAT":
    # load to data from csat
    with open('test.json') as json_file:
      data = json.load(json_file)
      
    
  elif tipoDeEncuesta == "bawr" or "BAWR":
    # load to data from bawr
    with open('test.json') as json_file:
      data = json.load(json_file)
      
  elif tipoDeEncuesta == "psur" or "PSUR":
   # load to data from psur
    with open('test.json') as json_file:
      data = json.load(json_file)
      
  else: 
    print("Ingrese una opción válida por favor")
    editarEncuesta(nombre,codigoCliente)
  

  for i in range(len(data)):
    print(data[i]["question"])
    print(data[i]["answers"])
    rspt = str(input("Ingrese respuesta: "))
    data[i]["respuestaSeleccionada"] = rspt

  resultados = {
    "nombre": nombre,
    "id":  idAsignado,
    "tipo": tipoDeEncuesta
  }
  resultados["encuestaRealizada"] = data

  
  with open("testResults.json") as fp:
    listObj = json.load(fp)
    listObj.append(resultados)
  with open("testResults.json", 'w') as json_file:
    json.dump(listObj, json_file, 
                        indent=4,  
                        separators=(',',': '))
 
    
  
  
def verResultados():
   f = open("testResults.json")
   data = json.load(f)
   print(data)
   # print(type(data[0]))
   key = "id"
   n = int(input("1: Desea ver resultados de un cliente en especifico.\n2: Desea ver una encuesta en particular\nElija: "))
   
   if n == 1:
    tipoDeEncuesta = str(input("Seleccione tipo de encuesta a buscar BAWR - CSAT - PSUR: "))
    key = "nombre"
    codigoDeCliente = int(input("Ingrese codigo de cliente: "))
    nombreAsignado = str(input("Ingrese nombre: "))
    encontrado = next(filter(lambda encontrado:encontrado.get(key) == nombreAsignado, data))
    print(encontrado)
   elif n == 2:
    key = "id"
    nombre = str(input("Ingrese id de la encuesta"))
    idAsignado = int(input("Ingrese id: "))
    encontrado = next(filter(lambda encontrado:encontrado.get(key) == idAsignado, data))
    print(encontrado)


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
    # this is solved
  elif opcion == 2:
    resolverEncuesta(nombre,codigoCliente)
    #this is what a i want to fix
  elif opcion == 3:
    verResultados()
main()
