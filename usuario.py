import os
import json

def fn_leer_cuentas_dict():
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r") as archivo:
            print("Archivos leidos correctamente")
            return json.load(archivo)
    else:
        print("No se ha encontrado usuarios.json")
    return {"usuarios": [] }