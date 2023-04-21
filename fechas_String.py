#Esta clase recibe una lista con solo las vacunas y extrae de ellas su fecha de aplicacion
#y retorna una lista con solo las fechas de tipo string
import re
from filtro_vacunas import Vacunas_aplicadas

class Fechas_string:

   
    def filtrar_fechas(self):
        
        vacunas = Vacunas_aplicadas().filtar()

        fecha_filtro = ''

        for i in range(len(vacunas)):

            fecha_filtro+= str(re.findall(r"[0-9]{2}-[0-9]{2}-[0-9]{4}",vacunas[i]))

        fechas_list= re.findall(r"[0-9]{2}-[0-9]{2}-[0-9]{4}",fecha_filtro)


        return fechas_list
        

    





