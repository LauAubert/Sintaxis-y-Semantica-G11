#Tad Cola

def crear_cola():
    #Crea una cola vacia
    return []
def es_vacia(cola):
    #Devuelve True si la cola esta vacia
    return len(cola)==0

def encolar_proc(cola,proc):
    #Encola un proceso al final de la lista
    cola.append(proc)

def desencolar_proc(cola):
    #Desencola un proceso del principio de la lista
    aux = cola[0]
    cola.pop(0)
    return aux

def ver_tam(cola):
    #Devuelve la cantidad de procesos en la cola
    return len(cola)

def copiar(cola1,cola2):
    #Copia los elementos de una cola a otra
    aux = crear_cola()
    while not es_vacia(cola2):
        proc = desencolar_proc(cola2)
        encolar_proc(aux,proc)
    while not es_vacia(aux):
        proc = desencolar_proc(aux)
        encolar_proc(cola1,proc)
        encolar_proc(cola2,proc)
    

