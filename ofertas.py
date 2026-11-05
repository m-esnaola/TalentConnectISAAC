import json
import os

# * Eskaintza guztiak JSON fitxategitik irakurtzen du
def fn_leer_ofertas_dict():
    """ Eskaintzak JSON fitxategitik irakurri eta hiztegi batean itzuliko du
    Fitxategia existitzen ez bada, eskaintza-zerrenda hutsa itzuliko du """

    if os.path.exists("ofertas.json"):
        
        with open("ofertas.json", "r", encoding="utf-8") as archivo:
            print("Archivos leidos correctamente")
            return json.load(archivo)
    else:
        print("No se ha encontrado el archivo con las ofertas")
        return {"ofertas": []}

# * Eskuragarri dauden eskaintza guztiak pantailan erakusten ditu
def fn_mostrar_ofertas_dict():
    """Eskuragarri dauden eskaintza guztiak eta haien eskakizunak pantailan erakutsi."""
    ofertas_dict = fn_leer_ofertas_dict()

    if not ofertas_dict["ofertas"]:
        print("No hay ofertas disponibles.")
        return
    
    print("\n========== OFERTAS DISPONIBLES ==========\n")
    for oferta_dict in ofertas_dict["ofertas"]:
        print("Oferta:", oferta_dict["titulo"])
        print("ID:", oferta_dict["id_oferta"])
        print("Salario:", oferta_dict["salario"],"€")
        print("Horario:", oferta_dict["horario"])

        print("\nRequisitos de la oferta:")
        print("Tecnologías requeridas: ")
        if not oferta_dict["tecnologias_requeridas"]:
            print("No se requiere ninguna tecnología")
        else:
            for tecnologia_str in oferta_dict["tecnologias_requeridas"]:
                print("-", tecnologia_str)

        print("Idiomas requeridos: ")
        if not oferta_dict["idiomas_requeridos"]:
            print("No se requieren idiomas específicos")
        else:
            for idioma_dict in oferta_dict["idiomas_requeridos"]:
                print("-", idioma_dict["nombre"], ":", idioma_dict["nivel"])

        print("\nCandidaturas recibidas:", len(oferta_dict["candidaturas"]))
        print("-----------------------------------------\n")

# TODO: Eskaintza jakin batean izena eman duten hautagaiak erakutsi
def fn_mostrar_candidtos_de_oferta():
    return

fn_mostrar_ofertas_dict()