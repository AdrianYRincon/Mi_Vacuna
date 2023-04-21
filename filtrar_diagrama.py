#Esta clase toma la lista con las fechas diagramadas y añade algunas cosas
#para que se vea mejor y tambie quita algunos datos innecesario
from diagramar_fechas import Diagramar_fechas
class Filtrar_diagrama:

    
    def filtrar_diagrama(self):
        diagrama = Diagramar_fechas().diagramar()

        indices = []        
                
        for i in range(len(diagrama)):

            if type(diagrama[i]) is int:
                indices.append(i)
                

    

        contador = 0

        for i in range(0,len(indices)):
            if i==0:
                diagrama.pop(indices[i])
                contador+=1
            else:
                diagrama.pop(indices[i]-contador)
                contador+=1

        cambio =''

        for i in range(0,len(diagrama)):

            if len(diagrama[i])==4:
                cambio = diagrama[i].replace(f"{diagrama[i]}",f"--{diagrama[i]}--")
                diagrama[i]=cambio
                
        return diagrama