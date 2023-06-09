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
    '''Crea un proceso vacio'''
    return [0,"","",0,0,datetime.datetime.now()]

def cargar_proceso(proc,pid:int,nom:str,tipo:str,tam:int,prio:int,fecha:str) -> bool:
    '''Carga la info del proceso'''
    proc[0] = pid
    proc[1] = nom
    proc[2] = tipo
    proc[3] = tam
    try:
        if prio < 1 or prio > 3: raise Exception
        proc[4] = prio
        proc[5] = datetime.datetime.strptime(fecha,'%d-%m-%Y %H:%M')
        return True
    except:
        return False



def mod_nom(proc,nom):
    '''Modifica el nombre del proceso'''
    proc[1] = nom

def mod_tipo(proc,tipo):
    '''Modifica el tipo del proceso'''
    proc[2] = tipo

def mod_tam(proc,tam):
    '''Modifica el tamano del proceso'''
    proc[3] = tam

def mod_prio(proc,prio):
    '''Modifica la prioridad del proceso'''
    proc[4] = prio

def ver_pid(proc):
    '''Devuelve el id del proceso'''
    return (proc[0])

def ver_nom(proc):
    '''Devuelve el nombre del proceso'''
    return (proc[1])

def ver_tipo(proc):
    '''Devuelve el tipo del proceso'''
    return (proc[2])

def ver_tam(proc):
    '''Devuelve el tamano del proceso'''
    return (proc[3])

def ver_prio(proc):
    '''Devuelve la prioridad del proceso'''
    return (proc[4])

def copiar(destino,origen):
    '''Copia los datos de un proceso a otro'''
    mod_nom(destino,ver_nom(origen))
    mod_prio(destino,ver_prio(origen))
    mod_tam(destino,ver_tam(origen))
    mod_tipo(destino,ver_tipo(origen))
    destino[5] = origen[5]

def ver_fecha(proc):
    '''Devuelve la fecha del proceso en formato dd-mm-yyyy hh:mm'''
    return proc[5].strftime("%d-%m-%Y %H:%M")

def ver_min(proc):
    '''Devuelve los minutos de la fecha del proceso'''
    return proc[5].minute

def ver_hora(proc):
    '''Devuelve la hora de la fecha del proceso'''
    return proc[5].hour

def ver_mes(proc):
    '''Devuelve el mes de la fecha del proceso'''
    return proc[5].month