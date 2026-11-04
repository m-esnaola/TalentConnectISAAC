import os
import json

#TODO: Dokumentatu funtzioak

def fn_leer_cuentas_dict():
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r",  encoding="utf-8") as archivo:
            print("Archivos leidos correctamente")
            return json.load(archivo)
    else:
        print("No se ha encontrado usuarios.json")
    return {"usuarios": [] }


def fn_crear_cuenta_dict():
    usuarios_dict = fn_leer_cuentas_dict()

    while True:
        nombre_str = input("Introduzca su nombre: ").strip().capitalize()
        if nombre_str:
            print("Nombre valido")
            break
        print("ERROR. El nombre no puede estar vacio.")

    while True:
        correo_str = input("Introduzca su correo: ").strip().lower()
        correo_valido_bool = fn_validacion_correo_bool(correo_str)
        if not correo_valido_bool:
            print("ERROR. El correo no es valido. Porfavor intentelo de nuevo")
            continue
        elif fn_buscar_correo_dict(correo_str, usuarios_dict["usuarios"]) is not None:
            print("ERROR. Este correo ya esta registrado")
            continue
        else:
            print("Correo Valido")
            break

    while True:
        contrasenia_str = input("Introduzca su contraseña: ").strip()
        if contrasenia_str:
            print("Contraseña Valida")
            break
        print("ERROR. La contraseña no puede estar vacía.")



    nuevo_usuario_dict = {
        "nombre": nombre_str,
        "correo": correo_str,
        "contrasenia": contrasenia_str
    }

    usuarios_dict["usuarios"].append(nuevo_usuario_dict)

    with open("usuarios.json","w",encoding="utf-8") as archivo:
        json.dump(usuarios_dict, archivo, indent=4)
    return nuevo_usuario_dict

#TODO: sesioa asteko funtzioa egin
def fn_iniciar_sesion_dict():

    usuarios_dict = fn_leer_cuentas_dict()
 
    usuario_actual_dict = None
    while usuario_actual_dict is None:
        correo_str = input("Introduzca su correo: ").strip()
        correo_valido_bool = fn_validacion_correo_bool(correo_str)
        if not correo_valido_bool:
            print("ERROR. El correo no es valido. Porfavor intentelo de nuevo.")
            continue
        usuario_actual_dict = fn_buscar_correo_dict(correo_str, usuarios_dict["usuarios"])
        if usuario_actual_dict is None:
            print("Ese correo no existe. Inténtelo de nuevo.")
            continue

    while True:
        contrasenia_str = input("Introduzca su contraseña: ").strip()
        if contrasenia_str == usuario_actual_dict["contrasenia"]:
            break
        print("Contraseña incorrecta. Intentelo de nuevo")

    return usuario_actual_dict

#Beste funtzioak datuak validatzeko#
#?Comprobatu ea validazioa ondo dagoen edo ez
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

def fn_buscar_correo_dict(correo, usuarios):
    for usuario_dict in usuarios:
        if correo.lower() == usuario_dict["correo"].lower():
            return usuario_dict
    return None

fn_crear_cuenta_dict()
fn_iniciar_sesion_dict()