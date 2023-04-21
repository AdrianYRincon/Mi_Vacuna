#Esta clase toma la lista clasificada y a los datos del mes que son de tipo str les asigna una
#variables que corresponde al nombre de ese mes y los datos tipo int que corresponder a la cantidad
#de aplicaciones de la vacuna segun el mes, se los agrega a la variable del mes con forma de *
#al multiplicar la cantidad de vacunas por *, de este manera generamos un tipo de diagrama
#por ultimo retornamos una lista con el diagrama de las vacunas
from clasificar import Clasificar

class Diagramar_fechas:


    def diagramar(self):

        clasificada = Clasificar().clasificar()

        enero = 'Ene:'
        febrero = 'Feb:'
        marzo = 'Mar:'
        abril = 'Abr:'
        mayo = 'May:'
        junio = 'Jun:'
        julio = 'Jul:'
        agosto = 'Ago:'
        septiembre = 'Sep:'
        octubre = 'Oct:'
        noviembre = 'Nov:'
        diciembre = 'Dic:'  


        for i in range(0,len(clasificada)):

            if type(clasificada[i]) is str:
                
                if clasificada[i]=='1':
                    clasificada[i]=enero
                elif clasificada[i]=='2':
                    clasificada[i]=febrero
                elif clasificada[i]=='3':
                    clasificada[i]=marzo
                elif clasificada[i]=='4':
                    clasificada[i]=abril
                elif clasificada[i]=='5':
                    clasificada[i]=mayo 
                elif clasificada[i]=='6':
                    clasificada[i]=junio
                elif clasificada[i]=='7':
                    clasificada[i]=julio
                elif clasificada[i]=='8':
                    clasificada[i]=agosto
                elif clasificada[i]=='9':
                    clasificada[i]=septiembre
                elif clasificada[i]=='10':
                    clasificada[i]=octubre
                elif clasificada[i]=='11':
                    clasificada[i]=noviembre
                elif clasificada[i]=='12':
                    clasificada[i]=diciembre
            else:
                clasificada[i-1]+='*'*clasificada[i]

        return clasificada