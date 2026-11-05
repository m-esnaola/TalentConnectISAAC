while(1 == 1):

    print("\nBienvenido al menú interactivo:")
    
    # Posibles cosas a añadir: 
        # Si es que da tiempo, o cara al futuro gestionar candidaturas (añadir nuevas)
        #Sacar estadisticas
        #Mi cuenta

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

    elif (selecion_int == 1):
        print("Opción de gestión de candidatos seleccionado")
        #Añadiria aqui un pequeño menu, con opciones como mostrar todos los candidatos, 
        #buscar un candidato concreto por ID o por algo en concreto y mostrar su informacion
        #filtar candidatos por x habilidades, idiomas o...
        
        #cada una de esas opciones, llamará a una función diferente en candidatos.py donde
        #ahí escribiremos todo el codigo de la funcion
        

    elif (selecion_int == 2):
        print("Opción de consulta de ofertas seleccionado")
        #Imprimiremos el nombre o lo basico de todas las ofertas que tengamos
        #el usuario elige una oferta en concreto, y se mostrara una lista de los candidatos
        #que se han presentado a esa oferta en concreto
        
        #esta opcion puede llamar a una funcion en un archivo nuevo llamado ofertas.py donde
        #gestionaremos todo el codigo de las funciones sobre ofertas, para mantener el codigo
        #mas seperado y legible

    elif (selecion_int == 3):
        print("Opción de gestión de procesos seleccionado")
        #Esta opcion puede llamar a una funcion en procesos_seleccion, donde dando el ID 
        #o algun dato de un candidato, podamos modificar su proceso de selección
        #por defecto todas las nuevas candidaturas estarán en revision, y se podrán cambiar
        #pendiente de entrevista, aceptado o rechazado

    else:
        print("Opción no válida")
        
    input("\nPulsa INTRO para volver al menú...")
