# creacion del archivo
inf = str(input('Ingrese texto: '))
file = open('./archivo.txt', 'w')
file.write(inf)
file.close()

# busqueda de la palabra

file2 = open('./archivo.txt', 'r')
data = file2.read()
buscar = str(input('Ingrese texto que busca: '))
cant = 0
for s in range(len(data)):
    lb = len(buscar) + s
    if (data[s:lb] == buscar):
        cant = cant + 1

print('palabra encontrada ' + str(cant) + ' veces')
