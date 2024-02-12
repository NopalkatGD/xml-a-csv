from xml.dom import minidom

path_file = minidom.parse("./archivos xml/archivo 1 copy.xml")

empleados = path_file.getElementsByTagName("empleado")
nombre_id = path_file.getElementsByTagName("nombre")

for empleado in empleados:
    id_empleado = empleado.getAttribute("id")
    print(id_empleado)

for nombre in nombre_id:
    id_name = nombre.getAttribute("att_test_2")
    print(id_name)