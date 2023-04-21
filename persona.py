#Esta clase toma la lista los vacunados con sus vacunas y extrae la
#informacion principal del vacunado y la organiza
import re

class Persona:
    
    def __init__(self,personal_info):


        math_obj = re.search(r"(.*),(.*),(.*),(.*),(.*)",personal_info)
        self.id_type = math_obj.group(1).strip()
        self.id =  math_obj.group(2).strip()
        self.surname =  math_obj.group(3).strip()
        self.name =  math_obj.group(4).strip()
        self.dateofbirth =  math_obj.group(5).strip()


    def __str__(self):
        
        return '<'+ self.name + ' '+ self.surname +' '+ self.id + ' '+ self.dateofbirth + '>'