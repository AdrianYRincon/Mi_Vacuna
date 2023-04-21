#Esta clase toma el string con la informacion de los vacunados
# y retorna una lista con esa informacion
from lector_documentos import Lector_Documentos

class Vacunados:

    def read_people(self):


        documento = Lector_Documentos("registraduria")

        lst = []

        tamaño_texto = len(documento.leer_documento())

        info = ""


        for i in range(0,tamaño_texto):
    
            if i<tamaño_texto-1:
                if documento.leer_documento()[i]=="\n" and documento.leer_documento()[i+1]=="\n":
                    lst.append(info)
                    info = ""
                else:
                    info+=documento.leer_documento()[i]
            if i==tamaño_texto-1:
                info+=documento.leer_documento()[i]
                lst.append(info)

        return lst


    



