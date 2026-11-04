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

def fn_crear_cuenta_dict():
    usuarios_dict = fn_leer_cuentas_dict

    nombre_str = input("Introduzca su nombre: ").strip().capitalize()
    while True:
        correo_str = input("Introduzca su correo: ").strip()
        correo_valido_bool = fn_validacion_correo_bool(correo_str)
        break

    return {}

extensiones_correo_set = {"com", "es", "eus", "org","net", "edu", "eu", "info", "io"}
def fn_validacion_correo_bool(correo):
    if correo.count("@") != 1 or " " in correo or ".." in correo:
        return False
    
    nombre_str, resto_str = correo.split("@")

    if "." not in resto_str:
        return False
    
    dominio_str, extension_str = resto_str.rsplit(".",1)
    if (nombre_str == "" or nombre_str.startswith(".") or nombre_str.endswith(".") or dominio_str == "" 
        or dominio_str.startswith(".") or dominio_str.endswith(".")):
        return False
    if extension_str.lower() not in extensiones_correo_set:
        return False
    return True

fn_crear_cuenta_dict()
