# -------Crear objetos de clase exp606Ejecucion.py

import exp06Estudiante as E

ec = E.Estudiante()

ec.nombre = 'Luis'
ec.apellido = 'Moreno Durand'

print("Nombre estudiante: " + ec.nombre + ' ' + ec.apellido)

ec.pension = 1523.2

ec.pagarPension()
