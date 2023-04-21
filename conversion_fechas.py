#Esta clase recibe una lista de fechas de tipo str
#y las convierte a tipo datetime para poder trabajar con ellas y retorna una lista de ellas
from datetime import datetime

class Conversion_fechas:

    
    def conversion(self,fechas):

        
        conversion_fechas = []

        for i in range(len(fechas)):
            conversion_fechas.append(datetime.strptime(fechas[i], '%d-%m-%Y'))

        return conversion_fechas
            
