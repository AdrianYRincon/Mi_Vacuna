#Esta clase recibe una lista con cada los datos de las vacunas aplicadas por persona, de alli
#toma cada elemento de la lista y busca el patron de fecha que debe repetirse por cada vacuna
#diferente y crear un arreglo que despues se va contando segun el numero de dosis que tenga y
#se le asinga esto a una variable, por ultimo usa un metodo que recibe como argumento el numero
#de dosis aplicadas, y retorna el numero de personas que tienen ese numero de dosis aplicadas
import re
from filtro_vacunas import Vacunas_aplicadas
class Dosis_aplicadas:


    def Consultar_numero_dosis(self,numero):
        vacunas = Vacunas_aplicadas().filtar()
                
        numero_dosis = []
        for i in range(len(vacunas)):
            numero_dosis.append(len(re.findall(r"[0-9]{2}-[0-9]{2}-[0-9]{4}",vacunas[i])))

        dosis1=0
        dosis2=0
        dosis3=0
        dosis4=0
        dosis5=0


        for i in range(len(numero_dosis)):

            if numero_dosis[i]==1:
                dosis1+=1
            if numero_dosis[i]==2:
                dosis2+=1
            if numero_dosis[i]==3:
                dosis3+=1
            if numero_dosis[i]==4:
                dosis4+=1
            if numero_dosis[i]==5:
                dosis5+=1
            


        

        if numero==1:
            return f"El numero de personas que tiene {numero} dosis aplicada es: {dosis1}"
        elif numero==2:
            return f"El numero de personas que tienen {numero} dosis aplicadas es: {dosis2}"
        elif numero==3:
            return f"El numero de personas que tienen {numero} dosis aplicadas es: {dosis3}"
        elif numero==4:
            return f"El numero de personas que tienen {numero} dosis aplicadas es: {dosis4}"
        elif numero==5:
            return f"El numero de personas que tienen {numero} dosis aplicadas es: {dosis5}"
        else:
            return "No pueden haber personas vacunadas con ese numero de dosis"