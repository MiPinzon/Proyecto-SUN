#Importamos sqlite3 para poder trabajar con bases de Datos de manera mas efectiva.
import sqlite3
import FuncionesSQL as funciones
import Graficador as graficar
import FuncionesGraficas as graficos
import os

database = sqlite3.connect("SUN.db")

lector = database.cursor()

try:
    lector.execute("CREATE TABLE ESTUDIANTES (NOMBRE VARCHAR(56), APELLIDO VARCHAR(24), ID VARCHAR(10) PRIMARY KEY, CODPDE INTEGER(4), ESTADO VARCHAR(10), PAPA INTEGER(2))")
except:
    pass

try:
    lector.execute("CREATE TABLE PROFESORES (NOMBRE VARCHAR(56), APELLIDO VARCHAR(24), ID VARCHAR(10) PRIMARY KEY, ESTADO VARCHAR(20))")
except:
    pass

try:
    lector.execute("CREATE TABLE MATERIAS (CODIGO VARCHAR(9) PRIMARY KEY, NOMBRE VARCHAR(30), CODFACULTAD INTEGER(4), CREDITOS INTEGER(1), PREREQ VARCHAR(30), CODPREREQ VARCHAR(9))")
except:
    pass

try:
    lector.execute('''CREATE TABLE MATERIASDOC (CODIGO VARCHAR(9), NOMBRE VARCHAR(30), NOMDOC VARCHAR(56), 
    APDOC VARCHAR(24), ID VARCHAR(10), HORARIOINIT INTEGER(4), HORARIOEND INTEGER(4), DIAS VARCHAR(10), CUPOS INTEGER(3), GRUPO INTEGER(2)) ''')
except:
    pass

try:
    lector.execute('''
    CREATE TABLE MATERIASEST (CODIGO VARCHAR(9), NOMBRE VARCHAR(30), IDEST VARCHAR(10), 
    NOMEST VARCHAR(56), APEST VARCHAR(24), GRUPO INTEGER(2), IDDOC VARCHAR(10), 
    NOMDOC VARCHAR(56), APDOC VARCHAR(24), HORARIOINIT INTEGER(4), 
    HORARIOEND INTEGER(4), DIAS VARCHAR(10), ESTATUS INTEGER(10), CALIFICACIÓN INTEGER(2))''')
except:
    pass
condition = True

os.system('cls')

while condition ==  True:

    opcion = graficar.Graficador(graficos.Menu)

    if (opcion == 1):

        opcion1 = graficar.Graficador(graficos.MenuAñadir)

        if (opcion1 == 1):
                funciones.AñadirEstudiante(lector,database)
        elif (opcion1 == 2):
                funciones.AñadirProfesor(lector,database)
        elif (opcion1 == 3):
                funciones.AñadirMateria(lector,database)
        elif (opcion1 == 4):
                pass
        else:
                print("Opcion no valida.")
            
        

    elif (opcion == 2):
        
        opcion2 = graficar.Graficador(graficos.MenuAsignar)
            

        if (opcion2 == 1):
                funciones.AsignarMaterias(lector,database)
        elif (opcion2 == 2):
                funciones.InscribirMaterias(lector,database)
        elif (opcion2 == 3):
                funciones.CancelarMaterias(lector,database)
        elif (opcion2 == 4):
                pass
        else:
            print("Opcion no valida.")

    elif (opcion == 3):
        
        opcion3 = graficar.Graficador(graficos.MenuModificar)

        if (opcion3 == 1):
            funciones.ModificarEstudiante(lector,database)
        elif (opcion3 == 2):
            funciones.ModificarProfesor(lector,database)
        elif (opcion3 == 3):
            pass
        else:
            print("Opcion no valida.")
    
    elif (opcion == 4):
        
        opcion4 = graficar.Graficador(graficos.MenuEliminar)

        if (opcion4 == 1):
            funciones.EliminarEstudiante(lector,database)
        elif (opcion4 == 2):
            funciones.EliminarProfesor(lector,database)
        elif (opcion4 == 3):
            pass
        else:
            print("Opcion no valida.")

    elif (opcion == 5):
        
        opcion5 = graficar.Graficador(graficos.MenuMostrar)

        if (opcion5 == 1):
            funciones.Mostrar(lector,"ESTUDIANTES")
        elif (opcion5 == 2):
            funciones.Mostrar(lector,"PROFESORES")
        elif (opcion5 == 3):
            funciones.Mostrar(lector,"MATERIAS")
        elif (opcion5 == 4):
            funciones.Mostrar(lector,"MATERIASDOC")
        elif (opcion5 == 5):
            funciones.Mostrar(lector,"MATERIASEST")
        elif (opcion5 == 6):
            pass
        else:
            print("Opcion no valida.")

    elif (opcion == 6):

        opcion6 = graficar.Graficador(graficos.MenuCalificaciones)

        if (opcion6 == 1):
            funciones.SubirCalificaciones(lector,database)
        elif (opcion6 == 2):
            funciones.CalcularPAPA(lector,database)
        elif (opcion6 == 3):
            pass
        else: print("Opcion no valida")
    
    elif(opcion == 7):

        opcion7 = graficar.Graficador(graficos.MenuBuscar)

        if (opcion7 == 1):
            funciones.BuscarEstudiante(lector,database)
        elif (opcion7 == 2):
            funciones.BuscarProfesor(lector,database)
        elif (opcion7 == 3):
            funciones.BuscarMateria(lector,database)
        elif (opcion7 == 4):
            pass
        else: print("Opcion no valida")

    elif (opcion == 8):
        condition = graficar.Graficador(graficos.Salir)

    else:
        print("Opcion no valida, escoga denuevo.")
database.commit()

database.close()