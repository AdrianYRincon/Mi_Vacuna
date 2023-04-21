#Esta clase toma una lista de fechas_convertidas de tipo datetime y los datos como el año y fecha
#los convierte en tipo str y va contando la cantidad de veces que se aplico la vacuna
#segun las fechas que indiquemos
#Retonornamos una lista con datos de los meses y años de en tipo str, pero la cantidad de veces
#que fue aplicada la vacuna segun los meses es de tipo int
from conversion_fechas import Conversion_fechas
from fechas_String import Fechas_string


class Clasificar:

    
    def clasificar(self):

        fechas = Fechas_string().filtrar_fechas()

        fechas_convertidas = Conversion_fechas().conversion(fechas)

        fechas_convertidas.sort()
        clasificadas = []
        contador=0
        
        for i in range(0,len(fechas_convertidas)):
            if i==0:
            
                contador+=fechas_convertidas[i].year
                clasificadas.append(str(contador))
                contador=0
                
                contador+=fechas_convertidas[i].month
                clasificadas.append(str(contador))
                contador=0

            if i<len(fechas_convertidas)-1:

                if fechas_convertidas[i].year!=fechas_convertidas[i+1].year:
                    
                    contador+=1
                    clasificadas.append(contador)
                    contador=0

                    contador+=fechas_convertidas[i+1].year
                    clasificadas.append(str(contador))
                    contador=0
                    
                    
                    contador+=fechas_convertidas[i+1].month
                    clasificadas.append(str(contador))
                    contador=0

                        
                
                elif fechas_convertidas[i].year==fechas_convertidas[i+1].year:

                    if fechas_convertidas[i].month==fechas_convertidas[i+1].month:
                        
                        contador+=1
                    
                        
                        
                    else:
                    
                        contador+=1
                        clasificadas.append(contador)
                        contador=0
                        
                        contador+=fechas_convertidas[i+1].month
                        clasificadas.append(str(contador))
                        contador=0

                        
                        
                    
            else:
            
                contador+=1
                clasificadas.append(contador)
            
        return clasificadas
