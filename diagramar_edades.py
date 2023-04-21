#Esta clase recibe una lista de la edades, les asigna una variable segun a la decada
#que corresponda y lleva un contador que va añadiendo un * segun el numero de
#vacunados en esa decada, por ultimo retorna una lista con el diagrama de los vacunados por
#decadas
from organizar_edades import Organizar_edades
class Diagramar_edades:


    def diagramar_edades(self):

        edades = Organizar_edades().Organizar()

        de0='1-10:'
        de1='10-20:'
        de2='20-30:'
        de3='30-40:'
        de4='40-50:'
        de5='50-60:'
        de6='60-70:'
        de7='70-80:'
        de8='80-90:'
        de9='90-100:'
        de10='>100:'

        for i in edades:
            
            if i>=1 and i<=10:
            
                de0+='*'
            if i>10 and i<=20:
                
                de1+='*'
            if i>20 and i<=30:
                
                de2+='*'
            if i>30 and i<=40:
                
                de3+='*'
            if i>40 and i<=50:
                
                de4+='*'
            if i>50 and i<=60:
                
                de5+='*'
            if i>60 and i<=70:
                
                de6+='*'
            if i>70 and i<=80:
                
                de7+='*'
            if i>80 and i<=90:
                
                de8+='*'
            if i>90 and i<=100:
                
                de9+='*'
            if i>100:
            
                de10+='*'


        lista_Edades = []

        lista_Edades.append(de0)
        lista_Edades.append(de1)
        lista_Edades.append(de2)
        lista_Edades.append(de3)
        lista_Edades.append(de4)
        lista_Edades.append(de5)
        lista_Edades.append(de6)
        lista_Edades.append(de7)
        lista_Edades.append(de8)
        lista_Edades.append(de9)
        lista_Edades.append(de10)

        return lista_Edades