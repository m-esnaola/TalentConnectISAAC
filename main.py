from candidatos import fn_añadir_candidato
from candidatos import fn_filtrar_candidatos
from candidatos import fn_mostrar_candidato_por_id
from candidatos import fn_mostrar_candidatos_dict
from ofertas import fn_mostrar_ofertas, fn_mostrar_candidatos_de_oferta
from usuario import fn_crear_cuenta_dict, fn_iniciar_sesion_dict


# * ERABILTZAILEAREN SARBIDE-MENUA
def fn_menu_acceso():
    """
    Erabiltzaileari saioa hasteko edo kontu berri bat sortzeko aukera eman.
    Saioa hasi ondoren edo kontua berria sortu eta gero, menu nagusira sartu.
    """
    while True:
        print("\n========== TALENTCONNECT ==========")
        print("0 --> Salir del programa")
        print("1 --> Iniciar sesión")
        print("2 --> Crear cuenta")

        seleccion_acceso_str = input("\nSeleccione una opción: ")
        if seleccion_acceso_str == "0":
            print("Adiós, vuelva pronto")
            break
        elif seleccion_acceso_str == "1":
            usuario_dict = fn_iniciar_sesion_dict()
            fn_menu_principal(usuario_dict)
        elif seleccion_acceso_str == "2":
            usuario_dict = fn_crear_cuenta_dict()
            fn_menu_principal(usuario_dict)
        else:
            print("ERROR. Opción no valida.")



def fn_menu_candidatos():
    while True:
        print("GESTION DE CANDIDATOS\n0. Volver al menu principal\n1. Mostrar todos los candidatos\n2. Buscar candidatos por ID\n3. Filtrar candidatos\n4. Añadir candidato")
        seleccion_candidatos_str=input("Seleccione una opcion:").strip()
        if seleccion_candidatos_str=="0":
            break
        elif seleccion_candidatos_str=="1":
            fn_mostrar_candidatos_dict()
        elif seleccion_candidatos_str=="2":
            fn_mostrar_candidato_por_id()
        elif seleccion_candidatos_str=="3":
            fn_filtrar_candidatos()
        elif seleccion_candidatos_str=="4":
            fn_añadir_candidato()
        else:
            print("Error , opcion no valida")


def fn_menu_ofertas():
    while True:
        print("CONSULTA DE OFERTAS\n0. Volver al menu principal\n1. Mostrar todas las ofertas\n2. Mostrar los candidatos de una oferta")
        seleccion_oferta_str=input("Seleccione una opcion: ").strip()
        if seleccion_oferta_str=="0":
            break
        elif seleccion_oferta_str=="1":
            fn_mostrar_ofertas()
        elif seleccion_oferta_str=="2":
            fn_mostrar_candidatos_de_oferta()
        else:
            print("Error , opcion no valida")


def fn_menu_procesos():
    """Hautaketa-prozesuak kudeatzeko azpimenua erakutsi."""
    while True:
        print("\n========== PROCESOS DE SELECCIÓN ==========")
        print("0 --> Volver al menú principal")
        print("1 --> Cambiar el estado de una candidatura")
        print("2 --> Consultar candidaturas por estado")

        seleccion_proceso_str = input("\nSeleccione una opción: ").strip()

        if seleccion_proceso_str == "0":
            break
        elif seleccion_proceso_str == "1":
            print("Todavía no implementado")
        elif seleccion_proceso_str == "2":
            print("Todavía no implementado")
        else:
            print("ERROR. Opción no válida.")

        
        



# * TALENTCONNECT MENU NAGUSIA
#TODO: funtzioak bukatu
def fn_menu_principal(usuario_dict):
    """
    Saioa hasi duen erabiltzaileari menu nagusia erakutsi.
    Hautagaiak, eskaintzak eta hautaketa-prozesuak kudeatzeko aukerak eskaini.

    Parametroak:
        usuario_dict (dict): Saioa hasi duen erabiltzailearen datuak.
    """
    while True:
        print("Menu principal")
        print("Bienvenido", usuario_dict["nombre"])
        print("0. Salir del menu")
        print("1. Gestion de candidatos")
        print("2. Consultar ofertas")
        print("3. Gestion de procesos de seleccion")

        seleccion_str=input("Seleccione una opcion:").strip()

        if seleccion_str=="0":
            break
        elif seleccion_str=="1":
            fn_menu_candidatos()
        elif seleccion_str=="2":
            fn_menu_ofertas()
        elif seleccion_str=="3":
            print
            #fn_menu_procesos() comentado porque aun no existe



# * PROGRAMAREN HASIERA
if __name__ == "__main__":
    fn_menu_acceso()