#Esta clase toma un string con todos los datos de vacunacion y extrae de la misma
#solo la fecha de nacimiento de los vacunados y retorna una lista con esos datos

from lector_documentos import Lector_Documentos
import re


class Filtar_fecha_nacimiento:


        def filtrar_fecha_nacimiento(self):

            texto = Lector_Documentos("registraduria").leer_documento()

            lista_vacunados = re.findall(r".*,[0-9]{2}-[0-9]{2}-[0-9]{4}",texto)
            match = []
            fecha = []

            for i in range(0,len(lista_vacunados)):
                match.append(re.search(r"[0-9]{2}-[0-9]{2}-[0-9]{4}",lista_vacunados[i]))


            for i in match:
                fecha.append(i.group(0))
            
            return fecha

    





