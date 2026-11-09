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

