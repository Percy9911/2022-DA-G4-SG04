#Experiencia de practica 5
#1.Escribir el siguiente código en el editor del lenguaje Python
def file_read(fname):
 txt = open(fname)
 print(txt.read())
print('text.txt')
file_read('test.txt')
print('\nabc.txt')
file_read('abc.txt')

#2.Describe el resultado de ejecutar la aplicación anteriormente ingresada
#Nos devuelve el contenido del txt
#3.Crear el archivo test.txt y volver a probar la aplicación