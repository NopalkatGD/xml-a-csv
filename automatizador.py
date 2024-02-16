import json
import os
import csv
from xml.dom import minidom
from os import path
from datetime import date

#declarar variables
Folio = ""
Fecha = ""
Nombre = ""
mes = ""
Receptor = ""

#Datos continuos
Solicitante = "Cruz Gregorio"
Entrega = "No"

path_files = "C:/Users/david.martinez/OneDrive - MCM Telecom/Obtener datos de facturación/Facturas/" #ruta de archivos xml a escanear
path_csv_out = "./salida csv/" #ruta de salida

csv_out = str(date.today())
print(csv_out)#Nombre del archivo
copy_num = 2

#listar contenido del directorio de entrada
ls_out_path = os.listdir(path_files)
ls_csv_path = os.listdir(path_csv_out)
#Nombre de las columnas de datos
columns = [["Archivo","Solicitante","Folio","Fecha","Nombre del emisor","Moneda","Subtotal","Importe","Total","Entrega en almacen","Concepto","Descripción"]]

#Comprobar existencia de archivo de salida
for out_files in ls_csv_path:
    print(out_files)
    if path.exists(path_csv_out+csv_out+".csv"):
        csv_out = str(date.today())+" ("+str(copy_num)+")"
        copy_num +=1
        print("este archivo ya existe")

#Generar Documento csv
with open(path_csv_out+csv_out+".csv","w",newline="") as salida:
    #Delimitadores del archivo
    writer = csv.writer(salida,delimiter=",")#el delimitador puede ser "," ";" "\t"

    #Darle nombres a las columnas
    #writer.writerows(columns)

    #Escanear archivos dentro del directorio
    for xml_files in ls_out_path:
        #Comprobar si los archivos son XML

        if os.path.isfile(os.path.join(path_files,xml_files)) and xml_files.endswith(".xml"):
            #Obtener las etiquetas del archivo
            contenido_xml = minidom.parse(path_files+xml_files)
            tag_1 = contenido_xml.getElementsByTagName("cfdi:Comprobante")
            tag_2 = contenido_xml.getElementsByTagName("cfdi:Emisor")
            tag_3 = contenido_xml.getElementsByTagName("cfdi:Traslado")
            tag_4 = contenido_xml.getElementsByTagName("cfdi:Concepto")
            #Obtener Atributos de las etiquetas
            for elements in tag_1:
                Folio = elements.getAttribute("Folio")
                Fecha = elements.getAttribute("Fecha")
                Moneda = elements.getAttribute("Moneda")
                Subtotal = elements.getAttribute("SubTotal")
                Total = elements.getAttribute("Total")

            for elements in tag_2:
                Nombre = elements.getAttribute("Nombre")

            for elements in tag_3:
                Importe = elements.getAttribute("Importe")

            for elements in tag_4:
                Concepto = elements.getAttribute("Descripcion")
                #Servicio = Concepto.split("-")

            #Crear Variable a partir de Concatenaciones
            FechaXstr = Fecha.split("-")

            #Obtener Fechas de archivo JSON
            with open("./Fechas/Fechas.json") as Content_date:
                # cargar fechas en una variable
                dates = json.load(Content_date)
                for meses in dates:
                    NumMes = meses.get("Numero")
                    if NumMes == FechaXstr[1]:
                        mes = meses.get("Mes")

            #Concatenación
            #Descripcion = str(FechaXstr[0] +" "+mes+" "+Nombre+" "+Servicio[0]+" "+Folio)
            #Descripcion = str(FechaXstr[0] + " " + mes + " " + Nombre + " " + Concepto + " " + Folio)
            Descripcion = str(FechaXstr[0] + " | " + mes + " | " + Nombre + " | " + Concepto + " | " + Folio)

            #Guardas los registros dentro del archivo CSV
            #"        Archivo","Solicitante","Folio","Fecha","Nombre del emisor","Moneda","Subtotal","Importe","Total","Entrega en almacen","Concepto","Descripcion"
            datos = [[xml_files,Solicitante,Folio,Fecha,Nombre,Moneda,Subtotal,Importe,Total,Entrega,Concepto,Descripcion]]

            writer.writerows(datos)
            print(datos)
print("Se ha creado el siguiente archivo: "+csv_out+".csv")
#sudo mv /* /dev/null