#Esta clase recibe una texto que contiene los datos de vacunacion para
#luego buscar en el mismo los nombres de las vacunas y ir llevando un conteo
#de las vacunas y al final retornar el nombre de la vacuna mas aplicada con 
#el numero de aplicaciones de la misma
import re
from lector_documentos import Lector_Documentos

class Vacuna_mas_aplicada:



    

    def consultar_vacuna(self):
        texto = Lector_Documentos("registraduria").leer_documento()
        

        sinovac= len(re.findall("sinovac", texto))
        sputnik= len(re.findall("sputnik", texto))
        AstraZeneca= len(re.findall("AstraZeneca", texto))
        Pfizer= len(re.findall("Pfizer", texto))
        Moderna= len(re.findall("Moderna", texto))
        Jansen= len(re.findall("Jansen", texto))

        cantida_vacunas = []
        cantida_vacunas.append(sinovac)
        cantida_vacunas.append(sputnik)
        cantida_vacunas.append(AstraZeneca)
        cantida_vacunas.append(Pfizer)
        cantida_vacunas.append(Moderna)
        cantida_vacunas.append(Jansen)

        cantida_vacunas.sort()

        mayor =cantida_vacunas[5]

        if mayor == sinovac:
            return f"La vacuna mas aplicada es la sinovac con una cantidad de {mayor} aplicaciones"
        elif mayor == sputnik:
            return f"La vacuna mas aplicada es la sputnik con una cantidad de {mayor} aplicaciones"
        elif mayor == Jansen:
            return f"La vacuna mas aplicada es la Jansen con una cantidad de {mayor} aplicaciones"
        elif mayor == Moderna:
            return f"La vacuna mas aplicada es la Moderna con una cantidad de {mayor} aplicaciones"
        elif mayor == Pfizer:
            return f"La vacuna mas aplicada es la Pfizer con una cantidad de {mayor} aplicaciones"
        elif mayor == AstraZeneca:
            return f"La vacuna mas aplicada es la Astrazeneca con una cantidad de {mayor} aplicaciones"

