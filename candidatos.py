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
        with open("candidatos.json", "r",  encoding="utf-8") as archivo:
            print("Archivos leidos correctamente")
            return json.load(archivo)
        
    # Fitxategia existitzen ez bada, hiztegi huts bat itzuli
    else:
        print("No se han encontrado candidatos en candidatos.json")
        return {"candidatos": []}


def fn_mostrar_candidatos_dict():

    #Eskuragarri dauden kandidatu guztiak pantailan erakutsi.

    total_candidatos_dict = fn_leer_candidatos_dict()

    
    if not total_candidatos_dict["candidatos"]:
        print("No hay candidatos registrados.")
        return
    
    print("\n========== CANDIDATOS DISPONIBLES ==========\n")
    for candidato_dict in total_candidatos_dict["candidatos"]:
        print("Id_candidato:", candidato_dict["id_candidato"])
        print("Nombre:", candidato_dict["nombre"])
        print("Email:", candidato_dict["email"])
        print("Telefono:", candidato_dict["telefono"])
        for tecnologia_dict in candidato_dict["tecnologias"]:
            print("Nombre:", tecnologia_dict["nombre"])
            print("Experiencia:", tecnologia_dict["experiencia"])
        for idioma_dict in candidato_dict["idiomas"]:
            print("Nombre:", idioma_dict["nombre"])
            print("Nivel:", idioma_dict["nivel"])

#Funcion para comprobar como se van imprimiendo:
#fn_mostrar_candidatos_dict()



# * Hautagai bat IDaren bidez bilatu eta bere informazioa erakutsi
def fn_mostrar_candidato_por_id():
    """Hautagai bat bere IDaren bidez bilatu eta haren informazio guztia pantailan erakutsi."""
    candidatos_dict = fn_leer_candidatos_dict()
    if not candidatos_dict["candidatos"]:
            print("No hay candidatos disponibles")
            return
    while True:
        opcion_candidato_str = input("Introduce el ID del candidato: ")
        if opcion_candidato_str.isdigit():
            opcion_candidato_int = int(opcion_candidato_str)
            break
        print("Introduce un ID numerico valido")
    for candidato_dict in candidatos_dict["candidatos"]:
        if opcion_candidato_int == candidato_dict["id_candidato"]:
            print("\n========== INFORMACIÓN DEL CANDIDATO ==========\n")
            print("ID:", candidato_dict["id_candidato"])
            print("Nombre:", candidato_dict["nombre"])
            print("Email:", candidato_dict["email"])
            print("Telefono:", candidato_dict["telefono"])
            print("\nTecnologías:")
            for tecnologia_dict in candidato_dict["tecnologias"]:
                print("-", tecnologia_dict["nombre"])
                print("  Experiencia:", tecnologia_dict["experiencia"], "años")

            print("\nIdiomas:")
            for idioma_dict in candidato_dict["idiomas"]:
                print("-", idioma_dict["nombre"])
                print("  Nivel:", idioma_dict["nivel"])

            print("===============================================\n")
            return
        
    print("No hay ningún candidato registrado con ese ID")


#TODO: Filtrar candidatos por tecnologías, idiomas y experiencia.
#Explicación de como hacerlo:
    #Hay 2 opciones de implementarlo:
        #1. Se pedira al usuario que escriba por pantalla la tecnologia, idioma y experiencia 
        #que quiere filtrar
        #2. Se pedira al usuario que elija por cual de las 3 opciones quiere filtrar
        # (tecnologia, idioma o experiencia) y luego se pedira que escriba por pantalla la 
        # tecnologia, idioma o experiencia que quiere filtrar
        #En ambos casos se comprobara si hay candidatos que cumplan con los filtros o no
        #Los que cumplan los requisitos se guardarán en una lista
        #Tras revisar todos los candidatos, se imprimira por pantalla la lista de candidatos
        #que cumplen los requisitos
    
def fn_filtrar_candidatos():
    candidatos_dict =fn_leer_candidatos_dict()
    tec_filtro_str=input("Introduce la tecnologia para filtrar: ").strip().lower()

    encontrado_bool = False
    for candidato_dict in candidatos_dict["candidatos"]:
        for tec_dict in candidato_dict["tecnologias"]:
            if tec_dict["nombre"].lower() == tec_filtro_str:
                print("ID:",candidato_dict["id_candidato"],"-",candidato_dict["nombre"],"-","Experiencia:",tec_dict["experiencia"],"años" )
                encontrado_bool=True
                break

    if not encontrado_bool:
        print("No se encontraron candidatos con esa tecnologia")



#TODO: Añadir candidatos
#Explicación de como hacerlo:
    #Se pedira al usuario que escriba por pantalla toda la información del candidato
    # (nombre, email, telefono, tecnologias, idiomas y experiencia)
    #Se comprobara que el ID del candidato no exista ya en el diccionario de candidatos
    #Si existe se mostrará un mensaje de error y se pedira al usuario que escriba otro ID
    #Si no existe se añadirá el candidato al diccionario de candidatos y se guardará en el archivo JSON
        #Para poder guardarlo en el arcivo JSON, primero tenremos que llamar a la funcion que lee
        #todas las candidaturas y guardarlos en una variable
        #Con nuestro nuevo candidato, se añadira a esa variable con .append()
        #Y se reescribe todo el archivo JSON
def fn_añadir_candidato():
    print()
    







    