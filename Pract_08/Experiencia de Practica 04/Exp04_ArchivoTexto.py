archivo = open('ArchivoNuevo04.txt','w')
opc=1;
while(opc==1):
    data= input("\nIngresar informacion al archvio: ")
    archivo.write(data)
    opc = int(input("Desea escribir otra linea en el archivo?: 1-yes   2-no : "))
archivo.close()



