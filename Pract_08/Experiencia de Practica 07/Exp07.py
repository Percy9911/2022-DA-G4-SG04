class Estudiante:
    
    curso = "Desarrollo de apps"
    mayor_edad= True
#metodo constructor
    def __init__(self, nombre, apellido, codigo):
        self.nombre= nombre
        self.apellido=apellido
        self.codigo=codigo
    @classmethod
    def getNombre (self) :
        return self.nombre
    def getcodigo (self) :
        return self.codigo
    def presentarse (self):
        return 'mi nombre es {} {} y mi codigo es {}'.format(self.nombre,self.apellido,self.codigo)
    def getApellido (self) :
        return self.apellido

#metodo destructor
    def __del__(self):
        print ('Estudiante eliminado')
#metodo estatico
    @staticmethod
    def mayor_edad ():
        return True

    
estudiante1 = Estudiante('Daniel','Oviedo',2020892671)
print (estudiante1.presentarse ())
print (estudiante1.mayor_edad ())
