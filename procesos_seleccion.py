import json
from ofertas import fn_leer_ofertas_dict
from candidatos import fn_leer_candidatos_dict

estados_list=["Pendiente de revision","Pendiente de entrevista","Aceptado","Rechazado"]

def fn_pedir_id_int(mensaje_str):
    while True:
        id_str=input(mensaje_str).strip()
        if id_str.isdigit():
            id_int=int(id_str)
            break
        else:
            print("Introduce un ID valido")
    return id_int

# * Eskaintza bat bilatu IDaren bidez
def fn_elegir_estado_str():
    """Egoeren zerrenda erakutsi eta erabiltzaileak aukeratutakoa itzuli."""
    print("\nEstados disponibles:")
    for i_int, estado_str in enumerate(estados_list, start=1):
        print(i_int, "-->", estado_str)

    while True:
        opcion_str = input("Seleccione un estado: ").strip()
        if opcion_str.isdigit() and 1 <= int(opcion_str) <= len(estados_list):
            estado_elegido_str = estados_list[int(opcion_str) - 1]
            break
        else:
            print("ERROR. Opcion no valida.")
    return estado_elegido_str

    # * Eskaintza bat bilatu IDaren bidez
def fn_buscar_oferta_dict(id_oferta_int,ofertas_int):
    """Id aren bidez eskaintza bilatu eta dict edo None itzuli"""
    for oferta_dict in ofertas_list:
        if oferta_dict["id_oferta"] == id_oferta_int:
            return oferta_dict
    """Eskaintza aurkitzen ez bada bueltatu none"""
    return None

# * Hautagaitza bat bilatu hautagaiaren IDaren bidez
def fn_buscar_candidatura_dict(id_candidato_int, candidaturas_list):
    """Hautagaiaren IDaren bidez hautagaitza bilatu eta dict edo None itzuli."""
    for candidatura_dict in candidaturas_list:
        if candidatura_dict["id_candidato"] == id_candidato_int:
            return candidatura_dict
    # Hautagaitza aurkitzen ez bada, None itzuli
    return None

    # * Hautagaitza baten egoera aldatu
    def fn_cambiar_estado_candidatura():
        """Eskaintza eta hautagai bat aukeratu eta haren hautagaitzaren egoera aldatu."""
        ofertas_dict = fn_leer_ofertas_dict()
        id_oferta_int=fn_pedir_id_int("Introduce el ID de la oferta:")
        oferta_dict=fn_buscar_oferta_dict(id_oferta_int,oferta_dict["ofertas"])

        if oferta_dict is None:
            print("No existe ninguna oferta con ese ID")
        else:
            id_candidato_int = fn_pedir_id_int("Introduce el id del candidato: ")
            candidatura_dict=fn_buscar_candidatura_dict(id_candidato_int,oferta_dict["candidaturas"])
            if candidatura_dict is None:
                print("Ese candidato no esta inscrito en esta oferta")
            else:
                print("\nEstado actual:", candidatura_dict["estado"])
                nuevo_estado_str = fn_elegir_estado_str()

                if nuevo_estado_str == candidatura_dict["estado"]:
                    print("La candidatura ya tiene ese estado")
                else:
                    # Egoera aldatu eta JSON fitxategia berridatzi
                    candidatura_dict["estado"] = nuevo_estado_str
                    with open("ofertas.json", "w", encoding="utf-8") as archivo:
                        json.dump(ofertas_dict, archivo, indent=4, ensure_ascii=False)
                    print("Estado actualizado correctamente")