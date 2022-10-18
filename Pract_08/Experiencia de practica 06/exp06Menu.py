# -------Crear una clase exp06-Menu.py

import exp06Estudiante as E

opc = 0
est = E.Estudiante()

while (opc != 4):
    print('-------- MENU --------')
    print('1. Matricular Alumno')
    print('2. Pagar pension Alumno')
    print('3. Imprimir informacion Alumno')
    print('4. Salir')

    opc = int(input('Opcion: '))

    if (opc == 1):
        est.matricular()
    elif (opc == 2):
        est.pagarPension()
    elif (opc == 3):
        est.imprimirDatos()
    else:
        print('Saliendo del programa...')
