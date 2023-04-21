#Esta clase recibe como argumento un nombre y una identificacion,
#la identificacion que reciba va a ser usada para buscar a la persona
#con esa identificacion en una lista de personas generada por otra clase
#cuando encuentre a la persona mostrara los datos de la misma con sus vacunas
#y creara un archivo txt que tendra como nombre el primer nombre de la persona y
#dentro de al archivo vendra los datos de que certifican su vacunacion como
#el nombre de la persona y el registro de vacunas

from vacunados import Vacunados
from gente import lista_gente
import re
from io import open

class Certificado:

    def __init__(self,nombre,identificacion):
        self.nombre = nombre

        self.identificacion = identificacion

    def Descargar_certificado(self):

       
        #Creamos un objeto para hacer una lista con los vacunados
        vacunados = Vacunados().read_people()
        #Hacemos una lista ordenada con solo los datos importantes de los vacunados
        personas = lista_gente().lista()        # print('\n')

        
        persona = ''

        

        for i in personas:

            if re.search(f"{self.identificacion}",str(i)):
                persona=i
                            

               
        indice_objeto =0 

        for i in range(len(vacunados)):
        
            if re.search(f"{self.identificacion}",vacunados[i]):
                

                
                indice_objeto=i

                
        contador=0    
        indice=0
        for i in range(len(vacunados[indice_objeto])):
            
            if i<len(vacunados[indice_objeto])-1:

                if vacunados[indice_objeto][i+1]=='\n' and contador<1:
                    
                    contador+=1
                    indice=i

        aux = ''


        for i in range(0,indice+1):
            aux+=vacunados[indice_objeto][i]
            
            

        vacunados[indice_objeto] = vacunados[indice_objeto].replace(f"{aux}",f"{persona}")

        self.nombre = open(f"{self.nombre}_certificado.txt","w")

        self.nombre.write("--Certificado Vacunacion--\r\n")

        self.nombre.write(f"{vacunados[indice_objeto]}")


        return f"{vacunados[indice_objeto]}"


    

        

