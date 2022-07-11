import time
import json
def main():
  with open('encuestas.json') as json_file:
    data = json.load(json_file)
    for i in data["BAWR"]:
      print(data["BAWR"].keys())
main()
