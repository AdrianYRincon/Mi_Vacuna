#Esta clase recibe una lista con la fecha de nacimiento de los vacunados,
#crea un objeto de la clase conversion_fecha para usar un metodo que me convierte las fechas en
#tipo datetime y con las fechas convertidas hace unas operaciones para calcular la edad del vacunado
# y retorna una lista con ellas
from conversion_fechas import Conversion_fechas
from datetime import date
from filtrar_fecha_nacimiento import Filtar_fecha_nacimiento
class Organizar_edades:


    def Organizar(self):

        fechas = Filtar_fecha_nacimiento().filtrar_fecha_nacimiento()
        conversion = Conversion_fechas().conversion(fechas)
        

        edades = []
        aux =0 

        for i in range(len(conversion)):
            aux = date.today().year-conversion[i].year
            aux -= ((date.today().month,date.today().day) < (conversion[i].month,conversion[i].day))
            edades.append(aux)
            aux=0


        return edades

