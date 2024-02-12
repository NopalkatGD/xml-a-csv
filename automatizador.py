import os
import csv
from xml.dom import minidom

#listar archivos
path_files = "./archivos xml/"
contenido = os.listdir(path_files)
res_csv = "./datos.csv"

#nombre de las columnas
columnas = [["id","nombre"]]


#crear archivo csv
with open(res_csv, "w", newline="") as resultado:
    writer = csv.writer(resultado, delimiter=",")#el delimitador puede ser "\t",";",","
    writer.writerows(columnas)
    for archivos in contenido:
        if os.path.isfile(os.path.join(path_files,archivos)) and archivos.endswith(".xml"):
        #leer archivos xml
            xml_file = minidom.parse(path_files+archivos)
            empresa = xml_file.getElementsByTagName("empresa")
            for empleado in empresa:
                #leer de otras etiquetas
                id_tag = empleado.getElementsByTagName("empleado")[0]
                name_tag = empleado.getElementsByTagName("nombre")[0]

                #obtener datos de los atributos
                att_id = id_tag.getAttribute("id")
                att_name = name_tag.getAttribute("att_test_2")

                print("-------------------------------------------------------------")
                print(att_id)
                print(att_name)

                #guarda los datos en el archivo csv
                datos = [[att_id,att_name]]
                writer.writerows(datos)

        #print(empresa)
