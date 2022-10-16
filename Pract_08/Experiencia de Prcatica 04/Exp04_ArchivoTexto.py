archivo = open('ArchivoNuevo04.txt','w')
opc=1;
while(opc==1):
    data= input("\nIngresar informacion al archvio: ")
    archivo.write(data)
    opc = int(input("Desea escribir otra linea en el archivo?: 1-yes   2-no : "))
archivo.close()



#archivo_bin = open('TipoBinnario','bw')
#bin=b'0x25'
#data= input("Ingresar informacion Binaria al archvio: ")
#archivo_bin.close()
