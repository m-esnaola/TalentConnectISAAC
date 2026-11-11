
import json
import os

#* Hautagaiak JSON fitxategitik irakurri.
def fn_leer_candidatos_dict():
    """
    Hautagaiak JSON fitxategitik irakurri eta hiztegi batean
    itzultzen ditu. Fitxategirik ez badago, zerrenda hutsa itzultzen du.
    """

    if os.path.exists("candidatos.json"):
        with open("candidatos.json", "r",  encoding="utf-8") as archivo:
            print("Archivos leidos correctamente")
            return json.load(archivo)
    else:
        print("No se han encontrado candidatos en candidatos.json")
        return {"candidatos": []}

#* Eskuragarri dauden kandidatu guztiak pantailan erakutsi.
def fn_mostrar_candidatos():

    """
    Erregistratutako hautagai guztiak pantailan erakusten ditu,
    haien datuak, teknologiak eta hizkuntzak barne.
    """

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


#* Hautagaiak teknologiaren arabera iragazi eta pantailan erakutsi.
def fn_filtrar_candidatos():
    """
    Hautagaiak sartutako teknologiaren arabera iragazten ditu,
    haien IDa, izena eta esperientzia erakutsiz.
    """
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


#* Hautagai berri bat gehitu eta JSON fitxategian gorde.
def fn_añadir_candidato():
    """
    Hautagai berri baten datuak eskatu eta erregistratzen ditu,
    IDa errepikatzen ez dela egiaztatuz.
    """
    candidatos_dict =fn_leer_candidatos_dict()

    id_str =input("Introduce el ID del candidato:").strip()
    if not id_str.isdigit():
        print("El id debe de ser un numero")
        return
    id_int=int(id_str)
    
    for c_dict in candidatos_dict["candidatos"]:
        if c_dict["id_candidato"] == id_int:
            print("Ese id ya existe")
            return
    
    nombre_str=input("Introduce el nombre: ").strip()
    email_str=input("Introduce el email: ").strip()
    # Telefonoa str motakoa da, JSON fitxategian horrela gordeta dagoelako.
    telefono_str=input("Introduce el numero de telefono: ").strip()

    nuevo_candidato_dict = {
        "id_candidato": id_int,
        "nombre": nombre_str,
        "email": email_str,
        "telefono": telefono_str,
        "tecnologias": [],
        "idiomas": []
    }
    candidatos_dict["candidatos"].append(nuevo_candidato_dict)
    with open("candidatos.json","w",encoding="utf-8")as archivo:
        json.dump(candidatos_dict,archivo,indent=4,ensure_ascii=False)
    print("Candidato añadido correctamente")
    







    