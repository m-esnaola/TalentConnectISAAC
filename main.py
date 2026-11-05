while(1 == 1):

    print("\nBienvenido al menú interactivo:")
    
    # Posibles cosas a añadir: 

    # Si es que da tiempo, o cara al futuro gestionar candidaturas (añadir nuevas)

    # Gestion de candidatos, mostrar todos los candidatos, buscar un candidato por id y 
    # mostrar su info...

    # Mostrar todos los candidatos que tiene una oferta (en concreto) -> Consultar Candidaturas

    # Gestionar procesos de seleccion --> cambiar el estado de una candidatura (pendiente de revision,
    # pendiente de entrevista, aceptado y rechazado)

    #Sacar estadisticas

    # Mi cuenta

    #Opciones más interesantes a añadir: gestion de candidatos, consultar candidaturas y gestionar procesos de seleccion
    #Darle prioridad a eso

    print("0 --> Salir del menú")
    print("1 --> Añadir candidato")
    print("2 --> Consultar candidato")
    print("3 --> Filtrar candidato")

    selecion_int = int(input(""))

    if (selecion_int == 0):
        print("Adiós, vuelva pronto")
        break

    elif (selecion_int == 1):
        print("Opción de añadir candidatos seleccionado")
        
        

    elif (selecion_int == 2):
        print("Opción de consulta de candidatos seleccionado")
     
        

    elif (selecion_int == 3):
        print("Opción de filtrado de candidatos seleccionado")


    else:
        print("Opción no válida")
        
    input("\nPulsa INTRO para volver al menú...")
