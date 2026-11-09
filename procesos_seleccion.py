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