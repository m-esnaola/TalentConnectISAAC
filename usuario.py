import os
import json

# * ENPRESAKO ERABILTZAILEEN KUDEAKETA

# * JSON fitxategitik enpresako erabiltzaileak irakurri
def fn_leer_cuentas_dict():
    """Erabiltzaileak JSON fitxategitik irakurri eta hiztegi batean itzuli."""
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r",  encoding="utf-8") as archivo:
            print("Archivos leidos correctamente")
            return json.load(archivo)
    # Fitxategia existitzen ez bada, hiztegi huts bat itzuli
    else:
        print("No se ha encontrado usuarios.json")
        return {"usuarios": [] }



# * Enpresako erabiltzaile-kontua sortu
def fn_crear_cuenta_dict():
    """Kontu berri bat sortu, datuak balioztatu eta JSON fitxategian gorde."""
    usuarios_dict = fn_leer_cuentas_dict()

    #Izena hutsik ez dagoela egiaztatu
    while True:
        nombre_str = input("Introduzca su nombre: ").strip().capitalize()
        if nombre_str:
            print("Nombre valido")
            break
        print("ERROR. El nombre no puede estar vacio.")

    #Posta elektronikoa balioztatu eta erregistratuta ez dagoela egiaztatu
    while True:
        correo_str = input("Introduzca su correo: ").strip().lower()
        # Posta elektronikoaren formatua balioztatzeko funtzioari deitu
        correo_valido_bool = fn_validacion_correo_bool(correo_str)
        if not correo_valido_bool:
            print("ERROR. El correo no es valido. Porfavor intentelo de nuevo")
            continue
        # Erabiltzailea bilatzeko funtzioari deitu, posta elektronikoa erregistratuta 
        # dagoen egiaztatzeko
        elif fn_buscar_correo_dict(correo_str, usuarios_dict["usuarios"]) is not None:
            print("ERROR. Este correo ya esta registrado")
            continue
        else:
            print("Correo Valido")
            break
    
    # Pasahitza hutsik ez dagoela egiaztatu
    while True:
        contrasenia_str = input("Introduzca su contraseña: ").strip()
        if contrasenia_str:
            print("Contraseña Valida")
            break
        print("ERROR. La contraseña no puede estar vacía.")

    # Erabiltzaile berriaren hiztegia sortu
    nuevo_usuario_dict = {
        "nombre": nombre_str,
        "correo": correo_str,
        "contrasenia": contrasenia_str
    }

    # Erabiltzaile berria zerrendara gehitu
    usuarios_dict["usuarios"].append(nuevo_usuario_dict)
    # Erabiltzaileen datuak JSON fitxategian gorde
    with open("usuarios.json","w",encoding="utf-8") as archivo:
        json.dump(usuarios_dict, archivo, indent=4)

    # ! Pasahitzak testu arruntean gordetzen dira
    # TODO: Pasahitzak hash seguruen bidez babestu denbora ematen badu

    return nuevo_usuario_dict ##
# * Kontua sortzeko funtzioaren amaiera



# * Erabiltzailearen saioa hasteko funtzioa
def fn_iniciar_sesion_dict():
    """Erabiltzailearen datuak egiaztatu eta haren hiztegia itzuli."""

    # JSON fitxategitik erregistratutako erabiltzaileak irakurri
    usuarios_dict = fn_leer_cuentas_dict()

    # Hasieran ez dago erabiltzaile hautaturik
    usuario_actual_dict = None
    # Posta elektronikoa baliozkoa eta erregistratuta dagoela egiaztatu
    while usuario_actual_dict is None:
        correo_str = input("Introduzca su correo: ").strip()
        # Posta elektronikoaren formatua balioztatzeko funtzioari deitu
        correo_valido_bool = fn_validacion_correo_bool(correo_str)
        
        if not correo_valido_bool:
            print("ERROR. El correo no es valido. Porfavor intentelo de nuevo.")
            continue

        # Erabiltzailea bilatzeko funtzioari deitu eta haren hiztegia eskuratu
        usuario_actual_dict = fn_buscar_correo_dict(correo_str, usuarios_dict["usuarios"])

        if usuario_actual_dict is None:
            print("Ese correo no existe.")
            continue
    
    # Sartutako pasahitza erabiltzailearen pasahitzarekin alderatu
    while True:
        contrasenia_str = input("Introduzca su contraseña: ").strip()
        if contrasenia_str == usuario_actual_dict["contrasenia"]:
            break
        print("Contraseña incorrecta. Intentelo de nuevo")

    # ! Pasahitzak testu arruntean alderatzen dira
    # TODO: Pasahitzen hash-ak egiaztatu denbora ematen badu
    # TODO: Saioa hasteko saiakera kopurua mugatu

    # Saioa hasi duen erabiltzailearen hiztegia itzuli
    return usuario_actual_dict
# * Saioa hasteko funtzioaren amaiera


# * DATUAK BALIOZTATZEKO ETA ERABILTZAILEAK BILATZEKO FUNTZIOAK

# Posta elektronikoetarako onartutako luzapenak
extensiones_correo_set = {"com", "es", "eus", "org","net", "edu", "eu", "info", "io"}
# * POSTA ELEKTRONIKOA BALIOZTATZEKO FUNTZIOA
def fn_validacion_correo_bool(correo):
    """Posta elektronikoaren formatua egiaztatu eta True edo False itzuli."""

     # @ ikur bakarra, espazioak eta bi puntu jarraian ez daudela egiaztatu
    if correo.count("@") != 1 or " " in correo or ".." in correo:
        return False
    
    # Posta elektronikoa @ ikurraren bidez bi zatitan banatu
    nombre_str, resto_str = correo.split("@")
    # Domeinuak gutxienez puntu bat duela egiaztatu
    if "." not in resto_str:
        return False
    
    # Azken puntutik domeinua eta luzapena banatu
    dominio_str, extension_str = resto_str.rsplit(".",1)
    # Izena eta domeinua hutsik ez daudela eta puntuak ondo kokatuta daudela egiaztatu
    if (nombre_str == "" or nombre_str.startswith(".") or nombre_str.endswith(".") or dominio_str == "" 
        or dominio_str.startswith(".") or dominio_str.endswith(".")):
        return False
    # Luzapena baimendutako multzoan dagoela egiaztatu
    if extension_str.lower() not in extensiones_correo_set:
        return False
    # TODO: Posta elektronikoaren balioztapena hobetu
    return True
# * Posta elektronikoa balioztatzeko funtzioaren amaiera 



# * POSTA ELEKTRONIKOAREN BIDEZ ERABILTZAILEA BILATZEKO FUNTZIOA
def fn_buscar_correo_dict(correo, usuarios):
    """Posta elektronikoaren bidez erabiltzailea bilatu eta dict edo None itzuli."""
    
    # Erabiltzaileen zerrenda zeharkatu eta posta elektronikoak alderatu
    for usuario_dict in usuarios:
        # Maiuskulak eta minuskulak bereizi gabe alderatu
        if correo.lower() == usuario_dict["correo"].lower():
            return usuario_dict
    # Erabiltzailea aurkitzen ez bada, None itzuli
    return None
# * funtzionaren amaiera