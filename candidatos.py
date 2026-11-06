#En este archivo, vamos a guardar el codigo de todas las funciones que requieran a los candidatos
#Ejemplos: 


 # - Mostrar todos los candidatos registrados.
        # - Buscar un candidato por ID y mostrar su información.
        # - Filtrar candidatos por tecnologías, idiomas y experiencia.
        # - Añadir candidatos
        
        # Las funcionalidades se implementarán en candidatos.py.
        # Cada opción del submenú llamará a una función diferente.



import json
import os
def fn_leer_candidatos_dict():

    #Erabiltzaileak JSON fitxategitik irakurri

    if os.path.exists("candidatos.json"):
        with open("usuarios.json", "r",  encoding="utf-8") as archivo:
            print("Archivos leidos correctamente")
            return json.load(archivo)
        
    # Fitxategia existitzen ez bada, hiztegi huts bat itzuli
    else:
        print("No se han encontrado candidatos en candidatos.json")
        return {"candidatos": []}


def fn_mostrar_candidatos_dict():

    #Eskuragarri dauden kandidatu guztiak pantailan erakutsi.

    total_candidatos_dict = fn_leer_candidatos_dict()

    
    if total_candidatos_dict["candidatos"] == False:
        print("No hay candidatos registrados.")
        return
    
    print("\n========== CANDIDATOS DISPONIBLES ==========\n")
    for candidato_dict in total_candidatos_dict["candidatos"]:
        print("Id_candidato:", candidato_dict["id_candidato"])
        print("Nombre:", candidato_dict["nombre"])
        print("Email:", candidato_dict["email"])
        print("Telefono:", candidato_dict["telefono"])

fn_mostrar_candidatos_dict()


    




    







    