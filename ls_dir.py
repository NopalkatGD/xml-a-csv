import os

ejemplo_dir = './archivos xml/'

contenido = os.listdir(ejemplo_dir)

for fichero in contenido:
    if os.path.isfile(os.path.join(ejemplo_dir, fichero)) and fichero.endswith('.xml'):
        print(fichero)