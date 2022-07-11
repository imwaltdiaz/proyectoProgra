import json
def main():
  test2 = {
    "cocaCola": {
      "encuesta 1": {
        "id": 53,
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
        "id": 22,
        "tipo": "bawr",
        "resultados": {
          "Te gusta el pan": "a"
        }
      }
    },
    "Pepsi": {
      "encuesta 1": {
        "id": 54,
        "tipo": "psur",
        "resultados": {
          "Pregunta 1": "Respuesta 1"
        }
      },
      "encuesta 2": {
        "id": 54,
        "tipo": "csat",
        "resultados": {
          "Pregunta 1": "Respuesta 1"
        }
        }
      },
  }
  bang = json.dumps(test2)
  f = open("dict.json","w")
  f.write(bang)
  f.close()
main()