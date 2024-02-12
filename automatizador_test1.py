import os
import csv
from xml.dom import minidom

#declarar variables
Folio = ""
Fecha = ""
Nombre = ""

#Ruta de los archivos xml a escanear
path_files = "./archivos xml/"

#listar contenido del directorio de entrada
ls_out_path = os.listdir(path_files)

#Nombre de las columnas de datos
columns = [["Archivo","Folio","Fecha","Nombre"]]

#Generar Documento csv
with open("./salida csv/datos.csv","w",newline="") as salida:
    #Delimitadores del archivo
    writer = csv.writer(salida,delimiter=",")#el delimitador puede ser "," ";" "\t"
    #Crear columnas
    writer.writerows(columns)

    #Escanear archivos dentro del directorio
    for xml_files in ls_out_path:
        #Comprobar si los archivos son XML
        if os.path.isfile(os.path.join(path_files,xml_files)) and xml_files.endswith(".xml"):

            #Obtener las etiquetas del archivo
            contenido_xml = minidom.parse(path_files+xml_files)
            tag_1 = contenido_xml.getElementsByTagName("cfdi:Comprobante")
            tag_2 = contenido_xml.getElementsByTagName("cfdi:Emisor")

            #Obtener Atributos de las etiquetas
            for elements in tag_1:
                Folio = elements.getAttribute("Folio")
                Fecha = elements.getAttribute("Fecha")
            print(Folio)
            print(Fecha)
            for elements in tag_2:
                Nombre = elements.getAttribute("Nombre")
            print(Nombre)

            #Guardas los registros dentro del archivo CSV
            datos = [[xml_files,Folio,Fecha,Nombre]]
            writer.writerows(datos)

#sudo mv /* /dev/null