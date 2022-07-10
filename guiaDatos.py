def main():
  test = [{
    "nombre":1,
    "codigo":2,
    "random":3,
    "tipoDeEncuesta": 4
  },{
    "id":2
  }]

  cliente = 205
  test2 = {
    "cocaCola": {
      "encuesta 1": {
        id: 53,
        "tipo": "csat",
        "resultados": {
          "Pregunta 1": {
            "respuesta": "Respuesta 1",
            "dificultad": 4
            },
          "Pregunta 2": {
            "respuesta": "Respuesta 2",
            "dificultad": 5
          },
          "Pregunta 3": {
            "respuesta": "Respuesta 3",
            "dificultad": 1
          }
        }
      },  
      "encuesta 2": {
        id: 22,
        "tipo": "bawr",
        "resultados": {
          "Pregunta 1": "Respuesta 1"
        }
      }
    },
    "Pepsi": {
      "encuesta 1": {
        id: 54,
        "tipo": "psur",
        "resultados": {
          "Pregunta 1": "Respuesta 1"
        }
      },
      "encuesta 2": {
        id: 54,
        "tipo": "csat",
        "resultados": {
          "Pregunta 1": "Respuesta 1"
        }
        }
      },
  }
  # fiu = test2["cocaCola"]
  # print(fiu)
  bang = sorted(test2["cocaCola"], key=lambda x: (test2["cocaCola"][x][id]))
  orden = bang
  mayor = orden[0]
  print(test2["cocaCola"][mayor])
  # print(orden)
  # print(test2["cocaCola"]["encuesta 1"][id])
  # print(bang)
main()