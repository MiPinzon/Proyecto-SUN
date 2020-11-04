import Graficador as graficar
import os
import FuncionesGraficas as graficos
# En esta funcion se añande los estdiantes a la base de datos
def AñadirEstudiante(lector,database):
    graficar.Simple()
    while True:
        try:
            a = input("Digite el nombre del nuevo estudiante: ")
            b = input("Digite el apellido del nuevo estudiante: ")
            c = input("Digite el ID del nuevo estudiante: ")
            d = int(input("Digite el codigo de la carrera del nuevo estudiante: "))
            e = input("Digite el estado del estudiante(Matriculado, Graduado, Perdida de cupo): ")
            f = int(input("Digite el P.A.P.A del estudiante: "))
            nuevo_usuario = (a,b,c,d,e,f)
            lector.execute("INSERT INTO ESTUDIANTES(NOMBRE, APELLIDO, ID, CODPDE, ESTADO, PAPA) VALUES(?,?,?,?,?,?)",nuevo_usuario)
            database.commit()
            break
        except:
            print("Ocurrido un error, por favor digite denuevo.")
    os.system('cls')
# En esta funcion se añande los profesores a la base de datos
def AñadirProfesor(lector,database):
    graficar.Simple()
    while True:
        try:
            a = input("Digite el nombre del nuevo docente: ")
            b = input("Digite el apellido del nuevo docente: ")
            c = input("Digite el ID del nuevo docente: ")
            d = "Docente"
            nuevo_docente = (a,b,c,d)
            lector.execute("INSERT INTO PROFESORES(NOMBRE, APELLIDO, ID, ESTADO) VALUES(?,?,?,?)",nuevo_docente)
            database.commit()
            break
        except:
            print("Ocurrido un error, por favor digite denuevo.")
    os.system('cls')
# En esta funcion se añande las materias a la base de datos
def AñadirMateria(lector,database):
    graficar.Simple()
    while True:
        a = input("Digite el codigo de la nueva materia: ")
        b = input("Digite el nombre de la nueva materia: ")
        c = input("Digite el codigo de la facultad a la que pertenece la materia: ")
        x = input("Digite el codigo del departamento que la dicta: ")
        d = int(input("Digite los creditos de la nueva materia: "))
        f = ""
        while True:
            e = input("Si tiene una materia prerequisito digite el codigo de esta, si no digite 0: ")
            lector.execute("SELECT * FROM MATERIAS WHERE CODIGO = ? ",(e,))
            if (len(lector.fetchall()) == 1):
                f = e
                lector.execute("SELECT NOMBRE FROM MATERIAS WHERE CODIGO = ?",(e,))
                e = lector.fetchall()
                e = ConvertirString(e)
                break
            elif (e == "0"):
                f = e
                e = "Sin prerequisito"
                break
            else:
                print("Materia no existente")
                if ("Y" == input("¿Desea ver las materias existentes Y||N?: ")):
                    Mostrar(lector,"MATERIAS")
                else:
                    pass
        break
    nueva_materia = (a,b,c,x,d,e,f)
    lector.execute("INSERT INTO MATERIAS(CODIGO, NOMBRE, CODFACULTAD, CODDEPA, CREDITOS, PREREQ, CODPREREQ) VALUES(?,?,?,?,?,?,?)",nueva_materia)
    database.commit()
    os.system('cls')
# Con esta funcion se le asignan las materias a los profesores
def AsignarMaterias(lector,database):
    graficar.Simple()
    while True:
        a = input("Digite el codigo de la materia a asignar: ")
        lector.execute("SELECT * FROM MATERIAS WHERE CODIGO = ?",(a,))
        if (len(lector.fetchall()) == 0):
            print("Materia no existente")
            if ("Y" == input("¿Desea ver las materias existentes Y||N?: ")):
                Mostrar(lector,"MATERIAS")
            else:
                break
        else:
            while True:
                e = input("Digite el ID del docente: ")
                lector.execute("SELECT * FROM PROFESORES WHERE ID = ?",(e,))
                if(lector.fetchall()==0):
                    print("Docente no encontrado")
                    if ("Y" == input("¿Desea ver los docentes disponibles Y||N?: ")):
                        Mostrar(lector,"PROFESORES")
                lector.execute("SELECT ESTADO FROM PROFESORES WHERE ID = ?",(e,))
                t = lector.fetchall()
                t = ConvertirString(t)
                if (t != "Docente"):
                    input("El profesor no esta dictando clases por el momento")
                    break
                else:
                    while True:
                        
                            lector.execute("SELECT NOMBRE FROM MATERIAS WHERE CODIGO = ?",(a,))
                            b = lector.fetchall()
                            b = ConvertirString(b)
                            lector.execute("SELECT NOMBRE FROM PROFESORES WHERE ID = ?",(e,))
                            c = lector.fetchall()
                            c = ConvertirString(c)
                            lector.execute("SELECT APELLIDO FROM PROFESORES WHERE ID = ?",(e,))
                            d = lector.fetchall()
                            d = ConvertirString(d)
                            f = int(input("Digite la hora de inicio de la clase (24h): "))
                            g = int(input("Digite la durancion de la clase: "))
                            h = input("Digite las iniciales de los dias de clase (L,M,C,J,V): ")
                            i = int(input("Digite el numero de cupos disponibles: "))
                            lector.execute("SELECT * FROM MATERIASDOC WHERE ID = ? AND DIAS = ?",(e,h,))
                            nueva_asignacion = (a,b,c,d,e,f,g,h,i)
                            lector.execute('''INSERT INTO MATERIASDOC(CODIGO, NOMBRE, NOMDOC, 
                            APDOC, ID, HORARIOINIT, HORASCLASE, DIAS, 
                            CUPOS) VALUES(?,?,?,?,?,?,?,?,?)''',nueva_asignacion)
                            database.commit()
                            break
                        
                    break
            break
    os.system('cls')
# Con esta funcion los estudiantes inscriben materias
def InscribirMaterias(lector,database):
    graficar.Simple()
    while True:
        a = input("Digite el codigo de la materia a inscribir: ")
        lector.execute("SELECT * FROM MATERIASDOC WHERE CODIGO = ?",(a,))
        if (len(lector.fetchall()) == 0):
            print("Materia no existente")
            if ("Y" == input("¿Desea ver las materias existentes Y||N?: ")):
                Mostrar(lector,"MATERIASDOC")
        lector.execute("SELECT CUPOS FROM MATERIASDOC WHERE CODIGO = ? AND CUPOS != 0",(a,))
        if (len(lector.fetchall()) == 0):
            input("No hay cupos disponibles para esta materia")
            break
        else:
            while True:
                c = input("Digite el ID del estudiante: ")
                lector.execute("SELECT * FROM ESTUDIANTES WHERE ID = ?",(c,))
                if(len(lector.fetchall()) == 0):
                    print("Estudiante no encontrado")
                    if ("Y" == input("¿Desea ver los estudiantes registrados Y||N?: ")):
                        Mostrar(lector,"ESTUDIANTES")
                lector.execute("SELECT ESTADO FROM ESTUDIANTES WHERE ID = ?",(c,))
                t = lector.fetchall()
                t = ConvertirString(t)               
                if(t != "Matriculado"):
                    input("El estudiante no esta en condicion de inscribir materias")
                    break
                lector.execute("SELECT CODPREREQ FROM MATERIAS WHERE CODIGO = ?",(a,))
                z = lector.fetchall()
                z = ConvertirString(z)               
                if (z != "0"): 
                    lector.execute("SELECT * FROM MATERIASEST WHERE CODIGO = ? AND IDEST = ? AND ESTATUS == 'Aprobado'",(z,c,))
                    y = lector.fetchall()
                    y = ConvertirLista(y)                  
                    if (z != "0" and  z not in y):
                        input("El estudiante no cumple con el prerequisito solicitado")
                        break
                    else:
                        prereq = True
                if (z == "0" or prereq == True):
                    while True:
                        try:
                            lector.execute("SELECT NOMBRE FROM MATERIAS WHERE CODIGO = ?",(a,))
                            b = lector.fetchall()
                            b = ConvertirString(b)
                            lector.execute("SELECT NOMBRE FROM ESTUDIANTES WHERE ID = ?",(c,))
                            d = lector.fetchall()
                            d = ConvertirString(d)
                            lector.execute("SELECT APELLIDO FROM ESTUDIANTES WHERE ID = ?",(c,))
                            e = lector.fetchall()
                            e = ConvertirString(e)                          
                            lector.execute("SELECT ID FROM MATERIASDOC WHERE CODIGO = ?",(a,))
                            g = lector.fetchall()
                            g = ConvertirString(g)
                            lector.execute("SELECT NOMDOC FROM MATERIASDOC WHERE CODIGO = ?",(a,))
                            h = lector.fetchall()
                            h = ConvertirString(h)
                            lector.execute("SELECT APDOC FROM MATERIASDOC WHERE CODIGO = ?",(a,))
                            i = lector.fetchall()
                            i = ConvertirString(i)
                            lector.execute("SELECT HORARIOINIT FROM MATERIASDOC WHERE CODIGO = ?",(a,))
                            j = lector.fetchall()
                            j = ConvertirNum(j)
                            lector.execute("SELECT HORASCLASE FROM MATERIASDOC WHERE CODIGO = ?",(a,))
                            k = lector.fetchall()
                            k = ConvertirNum(k)
                            lector.execute("SELECT DIAS FROM MATERIASDOC WHERE CODIGO = ?",(a,))
                            l = lector.fetchall()
                            l = ConvertirString(l)
                            m = "Cursando"
                            n = 0
                            nueva_asignacion = (a,b,c,d,e,g,h,i,j,k,l,m,n)
                            lector.execute('''INSERT INTO MATERIASEST(CODIGO, NOMBRE, IDEST, 
                            NOMEST, APEST,IDDOC, 
                            NOMDOC, APDOC, HORARIOINIT, 
                            HORASCLASE, DIAS, ESTATUS, CALIFICACIÓN) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)''',nueva_asignacion)
                            lector.execute("SELECT CUPOS FROM MATERIASDOC WHERE ID = ?",(g,))
                            o = lector.fetchall()
                            o = ConvertirNum(o)
                            o = o-1
                            lector.execute("UPDATE MATERIASDOC SET CUPOS = ? WHERE ID = ?",(o,g,))
                            database.commit()
                            break
                        except:
                            print("Ocurrido un error, digite denuevo porfavor.")                          
                    break
            break
    os.system('cls')
# Funcion para cancelar materias
def CancelarMaterias(lector,database):
    graficar.Simple()
    z = input("Digite el Id del estudiante: ")
    lector.execute("SELECT * FROM MATERIASEST WHERE IDEST = ?",(z,))
    y = lector.fetchall()
    if (len(y) == 0):
        ñ = input("El estudiante no tiene ninguna materia inscrita.")
    else:
        x = 0
        w = 14
        k = 0
        for i in range(len(y)):
            for j in y[i]:
                if (k == w):
                    k = 0
                    print("")
                print("|",end=" ")
                print(j,end=" ")
                print("|",end=" ")
                k = k + 1
        print(" ")
        y = input("Digite el codigo de la materia que desea eliminar: ")
        while True:
            try:
                lector.execute("DELETE FROM MATERIASEST WHERE IDEST = ? AND CODIGO = ?",(z,y,))
                break
            except:
                print("Codigo no existente.")
        database.commit()
    os.system('cls')
# Funcion para modificar un estudiante
def ModificarEstudiante(lector,database):
    graficar.Simple()
    z = input("Digite el ID del estudiante que desee modificar: ")
    lector.execute("SELECT * FROM ESTUDIANTES WHERE ID = ?",(z,))
    y = lector.fetchall()
    x = 0
    w = 6
    k = 0
    for i in range(len(y)):
        for j in y[i]:
            if (k == w):
                k = 0
                print("")
            print("|",end=" ")
            print(j,end=" ")
            print("|",end=" ")
            k = k + 1
    print("")
    graficos.MenuEstudiantes()
    while True:
        try:
            a = int(input("¿Que desea modificar del estudiante?"))
            break
        except:
            print("Opcion no valida, digite denuevo.")
    if (a == 1):
        b = input("Digite el nuevo nombre: ")
        lector.execute("UPDATE ESTUDIANTES SET NOMBRE = ? WHERE ID = ? ",(b,z,))
        lector.execute("UPDATE MATERIASEST SET NOMEST = ? WHERE IDEST = ?",(b,z,))
    if (a == 2):
        b = input("Digite el nuevo apellido: ")
        lector.execute("UPDATE ESTUDIANTES SET APEST = ? WHERE ID = ? ",(b,z,))
        lector.execute("UPDATE MATERIASEST SET APEST = ? WHERE IDEST = ?",(b,z,))
    if (a == 3):
        b = input("Digite el codigo de la nueva carrera: ")
        lector.execute("UPDATE ESTUDIANTES SET CODPDE = ? WHERE ID = ? ",(b,z,))
        lector.execute("DELETE FROM MATERIASEST WHERE IDEST = ?",(z,))
    if (a == 4):
        b = input("Digite el nuevo estado del estudiante: ")
        lector.execute("UPDATE ESTUDIANTES SET ESTADO = ? WHERE ID = ? ",(b,z,))
    if (a == 5):
        pass
    database.commit()
    os.system('cls')
# Funcion para modificar un profesor    
def ModificarProfesor(lector,database):
    graficar.Simple()
    z = input("Digite el ID del profesor que desee modificar: ")
    lector.execute("SELECT * FROM PROFESORES WHERE ID = ?",(z,))
    y = lector.fetchall()
    x = 0
    w = 4
    k = 0
    for i in range(len(y)):
        for j in y[i]:
            if (k == w):
                k = 0
                print("")
            print("|",end=" ")
            print(j,end=" ")
            print("|",end=" ")
            k = k + 1
    print("")
    graficos.MenuProfesor()
    while True:
        try:
            a = int(input("¿Que desea modificar del docente?"))
            break
        except:
            print("Opcion no valida, digite denuevo.")
    if (a == 1):
        b = input("Digite el nuevo nombre: ")
        lector.execute("UPDATE PROFESORES SET NOMBRE = ? WHERE ID = ? ",(b,z,))
        lector.execute("UPDATE MATERIASDOC SET NOMDOC = ? WHERE ID = ?",(b,z,))
        lector.execute("UPDATE MATERIASEST SET NOMDOC = ? WHERE IDEST = ?",(b,z,))
    if (a == 2):
        b = input("Digite el nuevo apellido: ")
        lector.execute("UPDATE PROFESORES SET APELLIDO = ? WHERE ID = ? ",(b,z,))
        lector.execute("UPDATE MATERIASDOC SET APDOC = ? WHERE ID = ?",(b,z,))
        lector.execute("UPDATE MATERIASEST SET APDOC = ? WHERE IDDOC = ?",(b,z,))
    if (a == 3):
        b = input("Digite el nuevo estado del docente: ")
        lector.execute("UPDATE PROFESORES SET ESTADO = ? WHERE ID = ? ",(b,z,))
        lector.execute("DELETE FROM MATERIASDOC WHERE ID = ?",(z,))
        lector.execute("DELETE FROM MATERIASEST WHERE IDDOC = ?",(z,))
    if (a == 4):
        pass
    database.commit()
    os.system('cls')
# Funcion para modificar una materia
def ModificarMaterias(lector,database):
    graficar.Simple()
    z = input("Digite el codigo de la materia que desee modificar: ")
    lector.execute("SELECT * FROM PROFESORES WHERE ID = ?",(z,))
    y = lector.fetchall()
    x = 0
    w = 14
    k = 0
    for i in range(len(y)):
        for j in y[i]:
            if (k == w):
                k = 0
                print("")
            print("|",end=" ")
            print(j,end=" ")
            print("|",end=" ")
            k = k + 1
    print("")
    graficos.MenuMaterias()
    while True:
        try:
            a = int(input("¿Que desea modificar del docente?"))
            break
        except:
            print("Opcion no valida, digite denuevo.")
    if (a == 1):
        b = input("Digite el nuevo nombre: ")
        lector.execute("UPDATE MATERIAS SET NOMBRE = ? WHERE ID = ? ",(b,z,))
        lector.execute("UPDATE MATERIASDOC SET NOMBRE = ? WHERE ID = ?",(b,z,))
        lector.execute("UPDATE MATERIASEST SET NOMBRE = ? WHERE IDEST = ?",(b,z,))
    if (a == 2):
        b = int(input("Digite el nuevo numero de creditos: "))
        lector.execute("UPDATE MATERIAS SET CREDITOS = ? WHERE ID = ? ",(b,z,))
    if (a == 3):
        pass
    database.commit()
    os.system('cls')
# Funcion para eliminar un estudiante
def EliminarEstudiante(lector,database):
    graficar.Simple()
    while True:
        try:
            z = input("Digite el ID del estudiante que desea eliminar: ")
            lector.execute("SELECT * FROM PROFESORES WHERE ID = ?",(z,))
            y = lector.fetchall()
            x = 0
            w = 4
            k = 0
            for i in range(len(y)):
                for j in y[i]:
                    if (k == w):
                        k = 0
                        print("")
                    print("|",end=" ")
                    print(j,end=" ")
                    print("|",end=" ")
                    k = k + 1
            a = input('''
            Advertencia: ¿Esta seguro de querer eliminar al usuario del sistema SUN? Toda la informacion se perdera
            sin posibilidad de ser recuperada Y||N: ''')
            b = input("Escriba la palabra 'Eliminar' para confirmar su ocpion: ")
            if(a == "Y" and b == "Eliminar"):
                lector.execute("DELETE FROM ESTUDIANTES WHERE ID = ? ",(z,))
                lector.execute("DELETE FROM MATERIASEST WHERE IDEST = ? ",(z,))
                database.commit()
                break
            else:
                input("Cancelando borrado de datos.")
                break
        except:
            print("Ocurrido un error, por favor digite denuevo")
    os.system('cls')
# Funcion para eliminar un profesor
def EliminarProfesor(lector,database):
    graficar.Simple()
    while True:
        try:
            z = input("Digite el ID del profesor que desea eliminar: ")
            lector.execute("SELECT * FROM PROFESORES WHERE ID = ?",(z,))
            y = lector.fetchall()
            x = 0
            w = 4
            k = 0
            for i in range(len(y)):
                for j in y[i]:
                    if (k == w):
                        k = 0
                        print("")
                    print("|",end=" ")
                    print(j,end=" ")
                    print("|",end=" ")
                    k = k + 1
            a = input('''
            Advertencia: ¿Esta seguro de querer eliminar al usuario del sistema SUN? Toda la informacion se perdera
            sin posibilidad de ser recuperada Y||N: ''')
            b = input("Escriba la palabra 'Eliminar' para confirmar su ocpion: ")
            if(a == "Y" and b == "Eliminar"):
                lector.execute("DELETE FROM PROFESORES WHERE ID = ? ",(z,))
                lector.execute("DELETE FROM MATERIASDOC WHERE ID = ? ",(z,))
                lector.execute("DELETE FROM MATERIASEST WHERE IDDOC = ? AND ESTATUS 'cursando' ",(z,))
                database.commit()
                break
            else:
                input("Cancelando borrado de datos")
                break
        except:
            print("Ocurrido un error, por favor digite denuevo")
    os.system('cls')
# Funcion para asinar una nota a los estudiantes           
def SubirCalificaciones(lector,database):
    graficar.Simple()
    z = input("Digite el Id del estudiante: ")
    lector.execute("SELECT * FROM MATERIASEST WHERE IDEST = ?",(z,))
    y = lector.fetchall()
    if (len(y) == 0):
        ñ = input("El estudiante no tiene ninguna materia inscrita.")
    else:
        x = 0
        w = 14
        k = 0
        for i in range(len(y)):
            for j in y[i]:
                if (k == w):
                    k = 0
                    print("")
                print("|",end=" ")
                print(j,end=" ")
                print("|",end=" ")
                k = k + 1
        print(" ")
        y = input("Digite el codigo de la materia que desea calificar: ")
        while True:
            try:      
                a = int(input("Digite la calificacion de la materia: "))
                lector.execute("UPDATE MATERIASEST SET CALIFICACIÓN = ? WHERE IDEST = ? AND CODIGO = ?",(a,z,y,))
                ''' if a>30:
                    lector.execute("SELECT CODIGO FROM MATERIASEST WHERE CALIFICACIÓN = ?",(a,))
                    b = lector.fetchall()
                    b = ConvertirString(b)
                    lector.execute("SELECT CODIGO FROM MATERIASEST WHERE CALIFICACIÓN = ?",(a,))
                    c = lector.fetchall()
                    c = ConvertirString(c)
                    materias_aprobada = (b,c)
                    lector.execute("INSERT INTO MATERIAAPRO (CODMATERIA, IDEST) VALUES = ?,?",materias_aprobada)
                    database.commit()'''
                break
            except:
                print("Codigo no existente.")
                break
        database.commit()
    os.system('cls')
# Con esta funcion se calcula el PAPA
def CalcularPAPA(lector,database):
    graficar.Simple()
    z = input("Digite el Id del estudiante: ")
    lector.execute("SELECT CODIGO FROM MATERIASEST WHERE IDEST = ?",(z,))
    y = lector.fetchall()
    y = ConvertirLista(y)
    l = []
    m = []
    for i in y:
        lector.execute("SELECT CREDITOS FROM MATERIA WHERE CODIGO = ?",(i,))
        a = lector.fetchall()
        a = ConvertirNum(a)
        m.append(a)
        lector.execute("SELECT CALIFICACIÓN FROM MATERIASEST WHERE CODIGO = ? AND IDEST = ? ",(i,z,))
        b = lector.fetchall()
        b = ConvertirNum(b)
        c = b*a
        l.append(c)
    n = sum(l)
    ñ = sum(m)
    p = n//ñ
    lector.execute("UPDATE ESTUDIANTES SET PAPA = ? WHERE ID = ?",(p,z,))
    database.commit()
    os.system('cls')
# Con esta funcion mostramos lo que hay en la base de datos
def Mostrar(lector,tabla):
    graficar.Simple()
    print("")
    b = 0
    c = "0"
    if (tabla == "ESTUDIANTES"):
        b = 6
        print('''
        1.) Nombre
        2.) Apellido
        3.) ID
        4.) PAPA
        ''')
        print("")
        d = int(input("Digite el orden que desea: "))
        if (d == 1):
            c = "NOMBRE"
            graficos.ImprimirTabla(tabla)
            lector.execute("SELECT * FROM ESTUDIANTES ORDER BY ?",(c,)) 
        if (d == 2):
            c = "APELLIDO"
            graficos.ImprimirTabla2(tabla)
            lector.execute("SELECT APELLIDO, NOMBRE, ID, CODPDE, ESTADO, PAPA FROM ESTUDIANTES") 
            
        if (d == 3):
            c = "ID"
            graficos.ImprimirTabla2(tabla)
            lector.execute("SELECT ID, NOMBRE, APELLIDO, CODPDE, ESTADO, PAPA FROM ESTUDIANTES") 
        if (d == 4):
            c = "PAPA" 
            graficos.ImprimirTabla2(tabla)
            lector.execute("SELECT PAPA, NOMBRE, APELLIDO, ID, CODPDE, ESTADO FROM ESTUDIANTES") 
    
    elif (tabla == "PROFESORES"):
        b = 4      
        print('''
        1.) Nombre
        2.) Apellido
        3.) ID
        ''')
        print("")
        d = int(input("Digite el orden que desea:"))
        if (d == 1):
            c = "NOMBRE"
            graficos.ImprimirTabla(tabla)
            lector.execute("SELECT * FROM PROFESORES ORDER BY ?",(c,))
        if (d == 2):
            c = "APELLIDO"
            graficos.ImprimirTabla(tabla)
            lector.execute("SELECT APELLIDO, NOMBRE, ID, ESTADO FROM PROFESORES")
        if (d == 3):
            c = "ID"
            graficos.ImprimirTabla2(tabla)
            lector.execute("SELECT ID, NOMBRE, APELLIDO, ESTADO FROM PROFESORES")

    elif (tabla == "MATERIAS"):
        b = 7
        print('''
        1.) Nombre
        2.) Codigo
        ''')
        print("")
        d = int(input("Digite el orden que desea:"))
        if (d == 1):
            c = "NOMBRE"
            graficos.ImprimirTabla(tabla)
        lector.execute("SELECT * FROM MATERIAS ORDER BY ?",(c,))
        if (d == 2):
            c = "CODIGO"
            graficos.ImprimirTabla2(tabla)
            lector.execute("SELECT CODIGO, NOMBRE, APELLIDO, CODFACULTAD, CODDEPA, CREDITOS, PREREQ, CODPREREQ FROM PROFESORES")
      
    elif (tabla == "MATERIASDOC"):
        b = 9
        print('''
        1.) Nombre de materia
        2.) Codigo de materia
        3.) Nombre de docente
        4.) Apellido de doncente
        5.) Id de docente
        ''')
        print("")
        d = int(input("Digite el orden que desea:"))
        if (d == 1):
            c = "NOMBRE"
            graficos.ImprimirTabla2(tabla)
            lector.execute("SELECT  NOMBRE, CODIGO, NOMDOC, APDOC, ID, HORARIOINIT, HORASCLASE, DIAS, CUPOS FROM MATERIASDOC")
        if (d == 2):
            c = "CODIGO"
            graficos.ImprimirTabla(tabla)
            lector.execute("SELECT CODIGO, NOMBRE, NOMDOC, APDOC, ID, HORARIOINIT, HORASCLASE, DIAS, CUPOS FROM MATERIASDOC")
        if (d == 3):
            c = "NOMDOC"
            graficos.ImprimirTabla2(tabla)
            lector.execute("SELECT NOMDOC, APDOC, CODIGO, NOMBRE, ID, HORARIOINIT, HORASCLASE, DIAS, CUPOS FROM MATERIASDOC")
        if (d == 4):
            c = "APDOC"
            graficos.ImprimirTabla2(tabla)
            lector.execute("SELECT APDOC, NOMDOC, CODIGO, NOMBRE, ID, HORARIOINIT, HORASCLASE, DIAS, CUPOS FROM MATERIASDOC")
        if (d == 5):
            c = "IDDOC"
            graficos.ImprimirTabla2(tabla)
            lector.execute("SELECT ID, APDOC, NOMDOC, CODIGO, NOMBRE,  HORARIOINIT, HORASCLASE, DIAS, CUPOS FROM MATERIASDOC")
        
    elif (tabla == "MATERIASEST"):
        b = 14
        print('''
        1.) Id estudiante
        2.) Codigo de materia
        ''')
        print("")
        d = int(input("Digite el orden que desea:"))
        if (d == 1):
            c = "NOMBRE"
            graficos.ImprimirTabla2(tabla)
            lector.execute("SELECT  IDEST, CODIGO FROM  MATERIASEST")
        if (d == 2):
            c = "CODIGO"
            graficos.ImprimirTabla2(tabla)
            lector.execute("SELECT CODIGO, IDEST FROM  MATERIASEST")
        if (d == 3):
            c = "NOMDOC"
            graficos.ImprimirTabla2(tabla)
            lector.execute("SELECT NOMDOC, APDOC, IDDOC, NOMBRE, CODIGO, NOMEST, APEST, IDEST, HORARIOINIT, DIAS, ESTATUS, CALIFICACIÓN FROM  MATERIASEST")
        if (d == 4):
            c = "APDOC"
            graficos.ImprimirTabla2(tabla)
            lector.execute("SELECT APDOC, NOMDOC, IDDOC, NOMBRE, CODIGO, NOMEST, APEST, IDEST, HORARIOINIT, DIAS, ESTATUS, CALIFICACIÓN FROM  MATERIASEST")
        if (d == 5):
            c = "NOMEST"
            graficos.ImprimirTabla2(tabla)
            lector.execute("SELECT NOMEST, APEST, IDEST, NOMBRE, CODIGO, NOMDOC, APDOC, IDDOC, HORARIOINIT, DIAS, ESTATUS, CALIFICACIÓN FROM  MATERIASEST")
        if (d == 6):
            c = "APEST"
            graficos.ImprimirTabla2(tabla)
            lector.execute("SELECT APEST, NOMEST, NOMBRE, CODIGO, IDEST, IDDOC, NOMDOC, APDOC, HORARIOINIT, DIAS, ESTATUS, CALIFICACIÓN FROM  MATERIASEST")
        if (d == 7):
            c = "IDDOC"
            graficos.ImprimirTabla2(tabla)
            lector.execute("SELECT  IDDOC, NOMDOC, NOMBRE, CODIGO, IDEST, NOMEST, APEST, APDOC, HORARIOINIT, DIAS, ESTATUS, CALIFICACIÓN FROM  MATERIASEST")
        if (d == 8):
            c = "IDEST"
            graficos.ImprimirTabla(tabla)
            lector.execute("SELECT IDEST, NOMEST, APEST, NOMBRE, CODIGO, IDDOC, NOMDOC, APDOC, HORARIOINIT, DIAS, ESTATUS, CALIFICACIÓN FROM  MATERIASEST")
    a = lector.fetchall()
    k = 0
    for i in range(len(a)):
        for j in a[i]:
            if (k == b):
                k = 0
                print("")
            print("|",end=" ")
            print(j,end=" ")
            print("|",end=" ")
            k = k + 1
    wait = input()
    os.system('cls')

def BuscarEstudiante(lector,database):
    graficar.Simple()
    print("")
    print('''
    1.) Nombre
    2.) Apellido
    3.) Id
    4.) PAPA 
    ''')
    print("")
    d = []
    a = int(input("Digite la opcion de busqueda: "))
    if(a == 1):
        c = input("Digite el nombre del estudiante: ")
        lector.execute("SELECT * FROM ESTUDIANTES WHERE NOMBRE = ?",(c,))
        d = lector.fetchall()
        graficos.ImprimirTabla("ESTUDIANTES")

    if (a == 2):
        c = input("Digite el Apellido del estudainte: ")
        lector.execute("SELECT * FROM ESTUDIANTES WHERE APELLIDO = ?",(c,))
        d = lector.fetchall()
        graficos.ImprimirTabla("ESTUDIANTES")

    if (a == 3):
        c = int(input("Digite el Id del estudiante: "))
        lector.execute("SELECT * FROM ESTUDIANTES WHERE ID = ?",(c,))
        d = lector.fetchall()
        graficos.ImprimirTabla("ESTUDIANTES")

    if (a == 4):
        c = int(input("Digite el PAPA del estudiante: "))
        lector.execute("SELECT * FROM ESTUDIANTES WHERE PAPA = ?",(c,))
        d = lector.fetchall()
        graficos.ImprimirTabla("ESTUDIANTES")

    b = 6
    k = 0
    for i in range(len(d)):
        for j in d[i]:
            if (k == b):
                k = 0
                print("")
            print("|",end=" ")
            print(j,end=" ")
            print("|",end=" ")
            k = k + 1
    wait = input()
    os.system('cls')
           
def BuscarProfesor(lector,database):
    graficar.Simple()
    print("")
    print('''
    1.) Nombre
    2.) Apellido
    3.) Id
    ''')
    print("")
    a = int(input("Digite la opcion de busqueda: "))
    d = []
    if(a == 1):
        c = input("Digite el nombre del Profesor: ")
        lector.execute("SELECT * FROM PROFESORES WHERE NOMBRE = ?",(c,))
        graficos.ImprimirTabla("PROFESORES")        
        d = lector.fetchall()
        b = 4
        k = 0
        for i in range(len(d)):
            for j in d[i]:
                if (k == b):
                    k = 0
                    print("")
                print("|",end=" ")
                print(j,end=" ")
                print("|",end=" ")
                k = k + 1
    if(a == 2):
        c = input("Digite el apellido del Profesor: ")
        lector.execute("SELECT * FROM PROFESORES WHERE APELLIDO = ?",(c,))
        graficos.ImprimirTabla("PROFESORES")   
        d = lector.fetchall()
        b = 4
        k = 0
        for i in range(len(d)):
            for j in d[i]:
                if (k == b):
                    k = 0
                    print("")
                print("|",end=" ")
                print(j,end=" ")
                print("|",end=" ")
                k = k + 1
    if(a == 3):
        c = int(input("Digite el Id del Profesor: "))
        lector.execute("SELECT * FROM PROFESORES WHERE ID = ?",(c,))
        graficos.ImprimirTabla("PROFESORES")   
        d = lector.fetchall()
        b = 4
        k = 0
        for i in range(len(d)):
            for j in d[i]:
                if (k == b):
                    k = 0
                    print("")
                print("|",end=" ")
                print(j,end=" ")
                print("|",end=" ")
                k = k + 1
    wait = input()
    os.system('cls')
    
def BuscarMateria(lector,database):
    graficar.Simple()
    print("")
    print('''
    1.) Nombre
    2.) Codigo
    ''')
    print("")
    a = int(input("Digite la opcion de busqueda: "))
    d = []
    if(a == 1):
        c = input("Digite el nombre de la materia: ")
        lector.execute("SELECT * FROM MATERIAS WHERE NOMBRE = ?",(c,))
        graficos.ImprimirTabla("MATERIAS")   
        d = lector.fetchall()
        b = 6
        k = 0
        for i in range(len(d)):
            for j in d[i]:
                if (k == b):
                    k = 0
                    print("")
                print("|",end=" ")
                print(j,end=" ")
                print("|",end=" ")
                k = k + 1
    if(a == 2):
        c = input("Digite el codigo de la materia: ")
        lector.execute("SELECT * FROM MATERIAS WHERE CODIGO = ?",(c,))
        graficos.ImprimirTabla("MATERIAS")   
        d = lector.fetchall()
        b = 6
        k = 0
        for i in range(len(d)):
            for j in d[i]:
                if (k == b):
                    k = 0
                    print("")
                print("|",end=" ")
                print(j,end=" ")
                print("|",end=" ")
                k = k + 1
    wait = input()
    os.system('cls')   

def ConvertirString(lista):
    tupla = lista[0]
    str = ''.join(tupla)
    return str

def ConvertirNum(lista):
    tupla = lista[0]
    num = int(''.join(map(str, tupla)))
    return num

def ConvertirLista(lista):
    nueva_lista=[]
    for i in lista:
        tupla = i
        a = ''.join(tupla)
        nueva_lista.append(a)
    return nueva_lista

def ConvertirListaNum(lista):
    nueva_lista=[]
    for i in lista:
        tupla = i
        a = int(''.join(map(str, tupla)))
        nueva_lista.append(a)
    return nueva_lista