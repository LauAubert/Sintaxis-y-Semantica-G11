# pid, nombre, tipo de proceso, tamaño, prioridad, fecha y hora de la última
# modificación
import datetime

#Proceso

p = [0,"","",0,0,0,0]
     
def crear_proceso():
    #Crea un proceso vacio
    return [0,"","",0,0,0]

def cargar_proceso(proc,pid,nom,tipo,tam,prio):
    #Carga la info del proceso
    proc[0] = pid
    proc[1] = nom
    proc[2] = tipo
    proc[3] = tam
    proc[4] = prio
    proc[5] = datetime.datetime.now()



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
