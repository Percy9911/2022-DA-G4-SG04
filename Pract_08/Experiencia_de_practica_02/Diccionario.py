
def mostrar_diccionario(a={}):
    print(a)
def añadir_diccionario(a={}):
    x=input('Ingrese la clave\n')
    y=input('Ingrese valor 1\n')
    z=input('ingrese valor 2\n')
    a[x]=[y,z]

materias = {}
materias["lunes"] = [6103, 7540]
materias["martes"] = [6201]
materias["miércoles"] = [6103, 7540]
materias["jueves"] = []
materias["viernes"] = [6201]
añadir_diccionario(materias)
mostrar_diccionario(materias)



