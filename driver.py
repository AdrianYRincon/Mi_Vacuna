
from numero_vacunados_fecha import Numero_vacunados
from filtrar_diagrama import Filtrar_diagrama
from consultar_num_edad import Consultar
from diagramar_edades import Diagramar_edades
from consultar_por_dosis import Dosis_aplicadas
from certificado_vacunacion import  Certificado
from vacuna_mas_aplicada import Vacuna_mas_aplicada

#Hacemos una lista ordenada con solo los datos importantes de los vacunados

opcion = int(input("""\n                   SERVICIOS MI VACUNA\n  
1. Consultar número de personas vacunadas en un lapso de tiempo dado. 
2. Ver diagrama del número de personas vacunadas en cada mes.
3. Consultar número de personas vacunadas en un rango de edad dado.
4. Ver diagrama del número personas vacunadas por rangos de edades (décadas).
5. Consultar número de personas vacunadas discriminando por número de dosis recibidas
6. Descargar el Certificado de Vacunación
7. Consultar vacuna más aplicada
Digite numero del servicio que desea:
"""))


if opcion == 1:
    numeros = Numero_vacunados()


    fecha = int(input("""
    1.Consultar por año
    2.Consultar por mes
    3.Consultar por dia
    Digite la opcion que va a consultar:"""))

    if fecha==1:
         #Recibe como argumento el año que desea consultar
        año = int(input("Digite el año que desea consultar:"))
       
        print(numeros.vacunado_año(año))

    elif fecha==2:
        #Recibe como argumento el año y mes que desea consultar
        año = int(input("Digite el año que desea consultar:"))
        mes= int(input("Digite el mes que desea consultar:"))
        print(numeros.vacunado_mes(año,mes))
    elif fecha==3:
        #Recibe como argumento el año, mes y dia que quiere consultar
        año = int(input("Digite el año que desea consultar:"))
        mes= int(input("Digite el mes que desea consultar:"))
        dia= int(input("Digite el dia que desea consultar:"))
        print(numeros.vacunado_dia(año,mes,dia)) 
    else:
       raise ValueError("Opcion invalida")
      

elif opcion==2:
    
    filtrar_diagrama = Filtrar_diagrama().filtrar_diagrama()

    for i in filtrar_diagrama:
        print(i)

  

elif opcion==3:
    #Recibe como argumento los dos numeros que definen el rango de edad a consultar

    edad = int(input("Digite el primer numero del rango:"))
    edad2 = int(input("Digite el segundo numero del rango:"))
    

    consultar_num_por_edad = Consultar().consultar_numero_por_edad(edad,edad2)

    print(consultar_num_por_edad)


elif opcion==4:


    diagramar_Edades = Diagramar_edades().diagramar_edades()

    for i in diagramar_Edades:
        print(i)

elif opcion==5:
    #Recibe como argumento el numero de dosis para la cual quiere saber el numero de personas vacunadas con tal numero de dosis

    dosis = int(input("Digite el numero de dosis que desea consultar:"))

    numero_dosis = Dosis_aplicadas()

    print(numero_dosis.Consultar_numero_dosis(dosis))


elif opcion==6:
    #Recibe como argumento el numero de documento y el nombre que sera utilizado para ponerlo como nombre en el archivo
    #texto creado con el certificado

    numero_documento = int(input("Digite su numero de documento:"))

    filename = input("Digite su primer nombre:")

    certificado = Certificado(filename,numero_documento)

    print(certificado.Descargar_certificado())

    print("Su certificado se ha descargado, puede revisar en los archivos de texto")
    

elif opcion==7:

    Vacuna_mas_aplicada = Vacuna_mas_aplicada()

    print(Vacuna_mas_aplicada.consultar_vacuna())


else:
    print("Esa opcion no existe")   

