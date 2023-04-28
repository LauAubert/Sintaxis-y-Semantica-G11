# pid, nombre, tipo de proceso, tamaño, prioridad, fecha y hora de la última
# modificación
import datetime

#Proceso

'''
0-PID (int)
1-Nombre (str)
2-Tipo (str)
3-Tamano (int)
4-Prioridad (int)
5-Fecha (datetime)
'''
     
def crear_proceso():
    #Crea un proceso vacio
    return [0,"","",0,0,datetime.datetime.now()]

def cargar_proceso(proc,pid:int,nom:str,tipo:str,tam:int,prio:int,mes:int,hora:int) -> None:
    #Carga la info del proceso
    proc[0] = pid
    proc[1] = nom
    proc[2] = tipo
    proc[3] = tam
    proc[4] = prio
    fechatemp = proc[5]
    proc[5] = datetime.datetime(
        fechatemp.year,
        mes,
        fechatemp.day,
        hora,
        fechatemp.hour,
        fechatemp.minute,
        fechatemp.second,
        )



def mod_nom(proc,nom):
    proc[1] = nom

def mod_tipo(proc,tipo):
    proc[2] = tipo

def mod_tam(proc,tam):
    proc[3] = tam

def mod_prio(proc,prio):
    proc[4] = prio

def ver_pid(proc):
    return (proc[0])

def ver_nom(proc):
    return (proc[1])

def ver_tipo(proc):
    return (proc[2])

def ver_tam(proc):
    return (proc[3])

def ver_prio(proc):
    return (proc[4])

def copiar(destino,origen):
    mod_nom(destino,ver_nom(origen))
    mod_prio(destino,ver_prio(origen))
    mod_tam(destino,ver_tam(origen))
    mod_tipo(destino,ver_tipo(origen))
    destino[5] = datetime.datetime.now()

def ver_fecha(proc):
    return proc[5].strftime("%d-%m %H:%M")

def ver_mes(proc):
    return proc[5].month

def ver_hora(proc):
    return proc[5].hour
