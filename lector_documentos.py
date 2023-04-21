#ESTA CLASE SE ENCARGA DE TOMAR UN DOCUMENTO DE TEXTO,LEERLO Y RETORNAR UN STRING
from io import open

class Lector_Documentos:

    def __init__(self,documento):
        self.documento = documento
        
    def leer_documento(self):
        archivo  = open(f"{self.documento}.txt","r")
        texto = archivo.read()
        archivo.close()

        return texto


