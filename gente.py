#Esta clase toma una lista con los vacunados y extrae solo la informacion personal del vacunado
from persona import Persona
from vacunados import Vacunados
class lista_gente:
 
    def lista(self):
        vacunados = Vacunados().read_people()
        gente = []
        
        for person in vacunados:
            p = Persona(person)
            gente.append(p)

        return gente
         