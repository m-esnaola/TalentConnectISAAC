#TODO: DOkumentazioa aldatu eta euskaraz jarri
while(1 == 1):

    print("\nBienvenido al menú interactivo:")
    
    # ? Posibles cosas a añadir: (si nos da tiempo)
    # - Si es que da tiempo, o cara al futuro gestionar candidaturas (añadir nuevas)
    # - Sacar estadisticas
    # - Mi cuenta

    print("0 --> Salir del menú")
    print("1 --> Gestión de candidatos")    #mostrar todos los candidatos, buscar un 
                                            #candidato por id y mostrar su info, filtar 
                                            #candidatos...
    print("2 --> Consultar oferta")         #Mostrar todos los candidatos que tiene una 
                                            #oferta (en concreto)
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
        
        # Las funcionalidades se implementarán en candidatos.py.
        # Cada opción del submenú llamará a una función diferente.

    # * CONSULTA DE OFERTAS
    elif (selecion_int == 2):
        print("Opción de consulta de ofertas seleccionado")
        # TODO (Maitane): Implementar la consulta de ofertas.
        # - Mostrar todas las ofertas disponibles.
        # - Permitir seleccionar una oferta mediante su ID.
        # - Mostrar los candidatos que se han postulado a esa oferta.

        # Las funciones se implementarán en ofertas.py.

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
