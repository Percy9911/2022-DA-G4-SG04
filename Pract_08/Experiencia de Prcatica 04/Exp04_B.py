def file_read(fname):
    with open(fname, "w") as myfile:
        myfile.write("Ejercicios Python\n")
        
    txt = open(fname)
    print(txt.read())
file_read('abc.txt')