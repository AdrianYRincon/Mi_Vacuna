#Esta clase toma la lista de vacunados completa y extrae de ella solo las vacunas aplicadas
#y retorna una lista de las mismas
from lector_documentos import Lector_Documentos
class Vacunas_aplicadas:


    def filtar(self):

        vacunados = Lector_Documentos("registraduria").leer_documento()
        fechas = []
        info_fechas = ''
        cont = 0
        
        for i in range(len(vacunados)):

            if i<len(vacunados)-1:

                if vacunados[i]=="\n" and vacunados[i+1]!="\n" and vacunados[i+1]!="c":
                    cont +=1
            
                if cont>=1:
                     info_fechas+=vacunados[i]
                

                if vacunados[i]=="\n" and vacunados[i+1]=="\n":
                    fechas.append(info_fechas)
                    cont=0
                    info_fechas=""

            if i==len(vacunados)-1:


                if vacunados[i]=="\n":
                    cont +=1
            
                if cont>=1:
                    info_fechas+=vacunados[i]
                    fechas.append(info_fechas)



        return fechas
