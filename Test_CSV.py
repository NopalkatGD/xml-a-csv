import csv

datos=[
    ["test1","test2"],
    ["test1.1","test2.1"],
    ["test1.2","test2.2"]
]

with open("./csv_test.csv","w",newline="") as archivo:
    writer = csv.writer(archivo,delimiter=',')
    writer.writerows(datos)