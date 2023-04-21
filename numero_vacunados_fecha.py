#Esta clase recibe una lista con las fechas de tipo datetime y con ellas
#hace operaciones para calcular las vacunas aplicadas segun el lapso
#de tiempo que le enviemos como argumento, y retorna como resultado
#el numero de vacunas aplicada segun el tiempo que le enviemos como
#argumento
from conversion_fechas import Conversion_fechas
from fechas_String import Fechas_string

class Numero_vacunados:
    

    def vacunado_año(self,año):

        string = Fechas_string().filtrar_fechas()


        fechas = Conversion_fechas().conversion(string)
        
        contador = 0
        for i in fechas:

            if i.year == año:

                contador+=1

        return f"el numero de vacunados en el año {año} es de = {contador}" 
    
       
               
    def vacunado_mes(self,año,mes):

        string = Fechas_string().filtrar_fechas()

        fechas = Conversion_fechas().conversion(string)
        
        contador2=0
        for i in fechas:

            if i.year == año and i.month==mes:

                contador2+=1

        return f"El numero de vacunados en el mes {mes} del año {año} es de = {contador2}"




    def vacunado_dia(self,año,mes,dia):

        string = Fechas_string().filtrar_fechas()
        
        fechas = Conversion_fechas().conversion(string)

        contador3=0
        for i in fechas:

            if i.year == año and i.month==mes and i.day==dia:
                contador3+=1


        return f"El numero de vacunados el dia {dia} del mes {mes} del año {año} es de = {contador3}"
        

    





