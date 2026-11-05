import json
import os

# * Eskaintza guztiak JSON fitxategitik irakurtzen du
def fn_leer_ofertas_dict():
    """ Eskaintzak JSON fitxategitik irakurri eta hiztegi batean itzuliko du
    Fitxategia existitzen ez bada, eskaintza-zerrenda hutsa itzuliko du """

    if os.path.exists("ofertas.json"):
        
        with open("ofertas.json", "r", encoding="utf-8") as archivo:
            print("Archivos leidos correctamente")
            return json.load(archivo)
    else:
        print("No se ha encontrado el archivo con las ofertas")
        return {"ofertas": []}

# TODO: Eskuragarri dauden eskaintza guztiak pantailan erakutsI
def fn_mostrar_ofertas_dict():
    return

# TODO: Eskaintza jakin batean izena eman duten hautagaiak erakutsi
def fn_mostrar_candidtos_de_oferta():
    return
