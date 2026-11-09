from ofertas import fn_mostrar_ofertas, fn_mostrar_candidtos_de_oferta
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
        print("\nBienvenido/a", usuario_dict["nombre"], "al menú interactivo:")
        # ? Posibles cosas a añadir: (si nos da tiempo)
        # - Sacar estadisticas
        # - Mi cuenta

        print("0 --> Salir del menú")
        print("1 --> Gestión de candidatos")    #mostrar todos los candidatos, buscar un 
                                                #candidato por id y mostrar su info, filtar 
                                                #candidatos y añadir candidatura
        print("2 --> Consultar oferta")
        print("3 --> Gestión de procesos de selección") #cambiar el estado de una candidatura 
                                                        #(pendiente de revision, pendiente de 
                                                        # entrevista, aceptado y rechazado)

        selecion_int = int(input(""))

        if (selecion_int == 0):
            print("Adiós, vuelva pronto")
            break

        # * GESTIÓN DE CANDIDATOS
        elif (selecion_int == 1):
            print("Opción de gestión de candidatos seleccionado")
            # TODO: Crear un submenú para gestionar candidatos.
            # - Mostrar todos los candidatos registrados.
            # - Buscar un candidato por ID y mostrar su información.
            # - Filtrar candidatos por tecnologías, idiomas y experiencia.
            # - Añadir candidatos
            
            # Las funcionalidades se implementarán en candidatos.py.
            # Cada opción del submenú llamará a una función diferente.

        # * ESKAINTZEN KONTSULTA
        elif (selecion_int == 2):
            print("Opción de consulta de ofertas seleccionado")
            # Eskaintzen kontsultarako azpimenua.
            while True:
                print("0. Volver al menú principal")
                print("1. Mostrar todas las ofertas")
                print("2. Mostrar todos los candidatos de una oferta")
                seleccion_oferta_str = input("Seleccione una opcion:")

                if seleccion_oferta_str == "0":
                    break
                elif seleccion_oferta_str == "1":
                    fn_mostrar_ofertas()
                elif seleccion_oferta_str == "2":
                    fn_mostrar_candidtos_de_oferta()
                else:
                    print("ERROR. Opción no valida. Porfavor, introduzca una opción valida")
                    
                

        # * GESTIÓN DE PROCESOS DE SELECCIÓN
        elif (selecion_int == 3):
            print("Opción de gestión de procesos seleccionado")
            # TODO: Implementar la modificación del estado de candidaturas.
            # - Identificar la oferta y el candidato.
            # - Consultar el estado actual de la candidatura.
            # - Permitir cambiar el estado: pendiente de revisión, pendiente de entrevista,
            #   aceptado o rechazado.

            # Las funciones se implementarán en procesos_seleccion.py.

        else:
            print("Opción no válida")
            
        input("\nPulsa INTRO para volver al menú...")

# * PROGRAMAREN HASIERA
if __name__ == "__main__":
    fn_menu_acceso()