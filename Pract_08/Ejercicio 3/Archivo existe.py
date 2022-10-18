import os
opc=1
while opc==1:
    x=input('Ingrese el nombre del archivo \n')
    r=os.path.isfile(x)
    if r==True:
        print("El archivo si existe")
    else:
        print("El archivo no existe")
    x=input("¿Desea comprobar otro archivo?\n si/no\n")
    if x=='no' or x=='No' or x=='NO' or x=='nO':
        opc=0
    
print('Programa Finalizado')
    

