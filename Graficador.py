import os

def Graficador(FuncionAGraficar):  
    Nombre_De_Programa = "Sistema Univesidad Nacional"
    logo = [
    "  ____    _   _   _   _ ", 
    " / ___|  | | | | | \ | |",
    " \___ \  | | | | |  \| |",
    "  ___) | | |_| | | |\  |",
    " |____/   \___/  |_| \_| "]
                            
    print(Nombre_De_Programa)
    for i in logo:
        print (i)
    print("")
    a = FuncionAGraficar()
    os.system('cls')
    return a

def Simple():
    Nombre_De_Programa = "Sistema Univesidad Nacional"
    logo = [
    "  ____    _   _   _   _ ", 
    " / ___|  | | | | | \ | |",
    " \___ \  | | | | |  \| |",
    "  ___) | | |_| | | |\  |",
    " |____/   \___/  |_| \_| "]
                            
    print(Nombre_De_Programa)
    for i in logo:
        print (i)
    print("")