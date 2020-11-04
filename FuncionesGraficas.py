def Menu():
    print("Bienvenido, seleccione la operacion que desea realizar")
    print("1.) Añadir")
    print("2.) Asignar||Adicionar||Cancelar Materias")
    print("3.) Modificar")
    print("4.) Eliminar usuario")
    print("5.) Mostrar bases de datos")
    print("6.) Calificar")
    print("7.) Buscar")
    print("8.) Salir")

    while True:
        try:
            opcion = int(input("Digite la opción: "))
            break
        except:
            print("Numero no valido, escoga denuevo.")
    return opcion

def MenuAñadir():
    while True:
        
            print("1.) Estudiante")
            print("2.) Profesor")
            print("3.) Materia")
            print("4.) Cancelar")
        
            while True:
                try:
                    opcion1 = int(input("Digite el tipo de dato a añadir: "))
                    break
                except:
                    print("Numero no valido, escoga denuevo.")
            return opcion1

def MenuAsignar():
    while True:
        
            print("1.) Asignar materia a profesor")
            print("2.) Inscribir materias para estudiante")
            print("3.) Cancelacion de una materia")
            print("4.) Cancelar")
        
            while True:
                try:
                    opcion2 = int(input("Digite la opcion que desea: "))
                    break
                except:
                    print("Numero no valido, escoga denuevo.")
            return opcion2

def MenuModificar():
    while True:
        
            print("1.) Estudiantes")
            print("2.) Profesor")
            print("3.) Materias")
            print("4.) Cancelar")
        
            while True:
                try:
                    opcion3 = int(input("Digite la opcion que desea: "))
                    break
                except:
                    print("Numero no valido, escoga denuevo.")
            return opcion3

def MenuEstudiantes():
    print("1.) Nombre")
    print("2.) Apellido")
    print("3.) Carrera")
    print("4.) Estado")
    print("5.) Cancelar")

def MenuProfesor():
    print("1.) Nombre")
    print("2.) Apellido")
    print("3.) Estado")
    print("4.) Cancelar")

def MenuMaterias():
    print("1.) Nombre")
    print("2.) Creditos")
    print("3.) Cancelar") 

def MenuEliminar():
    while True:
        
            print("1.) Estudiantes")
            print("2.) Profesor")
            print("3.) Cancelar")
        
            while True:
                try:
                    opcion4 = int(input("Digite la opcion que desea: "))
                    break
                except:
                    print("Numero no valido, escoga denuevo.")
            return opcion4

def MenuMostrar():
    while True:
        
            print("1.) Estudiantes")
            print("2.) Profesor")
            print("3.) Materias")
            print("4.) Materias asignadas a profesores")
            print("5.) Materias vistas por estudiante")
            print("6.) Cancelar")
        
            while True:
                try:
                    opcion5 = int(input("Digite la opcion que desea: "))
                    break
                except:
                    print("Numero no valido, escoga denuevo.")
            return opcion5

def MenuCalificaciones():
        while True:
        
            print("1.) Calificar materias")
            print("2.) Calcular PAPA")
            print("3.) Cancelar")
        
            while True:
                try:
                    opcion6 = int(input("Digite la opcion que desea: "))
                    break
                except:
                    print("Numero no valido, escoga denuevo.")
            return opcion6

def MenuBuscar():
        while True:
        
            print("1.) Buscar Estudiante")
            print("2.) Buscar Profesor")
            print("3.) Buscar Materia")
        
            while True:
                try:
                    opcion7 = int(input("Digite la opcion que desea: "))
                    break
                except:
                    print("Numero no valido, escoga denuevo.")
            return opcion7
   

def ImprimirTabla(tabla):
    if (tabla == "ESTUDIANTES"):
        print("Nombres"," ","Apellidos"," ","ID"," ","Codigo Plan de estudios"," ","Estado"," "," P.A.P.A.")
        print("")
        print("")
    if (tabla == "PROFESORES"):
        print("Nombres"," ","Apellidos"," ","ID"," ","Estado")
        print("")
        print("")
    if (tabla == "MATERIAS"):
        print("Codigo"," ","Nombre"," ","Codigo de Facultad"," ","Codigo plan de estudio"," ","Creditos"," "," Prerequisito"," ","Codigo del prerequisito")
        print("")
        print("")
    if (tabla == "MATERIASDOC"):
        print("Codigo"," ","Nombre"," ","Nombre Docente"," ","Apellido Docente"," ","ID"," "," Hora de inicio"," ","Horas clase"," ","Dias"," ","Cupos"," ","Grupo")
        print("")
        print("")
    if (tabla == "MATERIASEST"):
        print("Codigo"," ","Nombre"," ","ID Estudiante"," ","Nombre Estudiante"," ","Apellido Estudiante"," "," Grupo"," ","ID Profesor"," "," Nombre Profesor"," ","Apellido Profesor"," ","Hora final"," ","Dias"," ","Estatus"," ","Calificación")
        print("")
        print("")    


def ImprimirTabla2(tabla): 
    if (tabla == "ESTUDIANTES"):
        print("")
        print("")
    if (tabla == "PROFESORES"):
        print("")
        print("")
    if (tabla == "MATERIAS"):
        print("")
        print("")
    if (tabla == "MATERIASDOC"):
        print("")
        print("")
    if (tabla == "MATERIASEST"):
        print("Codigo materia"," ","id estudiante",)
        print("")
        print("")


def Salir():
    condition = True
    salida = input("Esta seguro que desea salir Y|N: ")
    if (salida == "Y"):
        condition = False
    else:
        pass
    return condition