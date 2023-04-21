#Esta clase recibe una lista con las edades de los vacunados y hace un metodo que recibe
#dos argumentos que corresponden al intervalo de años en el cual se quiere buscar el
#numero de vacunados y retorna el numero de vacunados en ese intervalo
from organizar_edades import Organizar_edades
class Consultar:


    def consultar_numero_por_edad(self,a,b):

        edades = Organizar_edades().Organizar()
        
        contador = 0

        if a>b:
            aux=a
            a=b
            b=aux

        for i in edades:

            if i>=a and i<=b:
                contador+=1

        return f"El numero de personas vacunadas entre los {a} y {b} años de edad es {contador}"
