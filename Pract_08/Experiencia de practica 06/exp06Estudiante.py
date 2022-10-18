# -------Crear una clase exp06Estudiante.py
class Estudiante:
    codigo = 0
    nombre = ''
    apellido = ''
    carrera = ''
    semestre = 0
    pension = 0.0
    deuda = 1

    def ingresarDatos(self):
        print('Ingrese informacion solicitada del estudiante')
        self.codigo = int(input('Codigo: '))
        self.nombre = str(input('Nombres: '))
        self.apellido = str(input('Apellidos: '))
        self.carrera = str(input('Carrera: '))
        self.semestre = int(input('Semestre: '))
        self.pension = float(input('Pension: '))

    def imprimirDatos(self):
        print('Informacion del estudiante')
        print('Codigo: ' + str(self.codigo))
        print('Nombres: ' + self.nombre)
        print('Apellidos: ' + self.apellido)
        print('Carrera: ' + self.carrera)
        print('Semestre: ' + str(self.semestre))
        print('Pension: ' + str(self.pension))

    def matricular(self):
        print('matricular alumno')
        self.ingresarDatos()
        print('FICHA DE MATRICULA')
        self.imprimirDatos()

    def pagarPension(self):
        if (self.deuda == 1):
            print('Pagar Pension')
            print('Monto: ' + str(self.pension))
            print('Pago procesado')
            self.deuda = 0
        else:
            print('ya se pago la pension')
