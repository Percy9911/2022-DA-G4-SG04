# -------Crear un archivo de texto

file = open("./texto.txt", "w")
file.close()

# --------Crear un archivo de tipo binario

file2 = open("./binario.bin", "wb")
file2.close()

# -------Abrir un archivo para escritura

file = open("./texto.txt", "w")
file.write("Esto es un texto")
file.close()
