
def crear_cola():
    return []
def es_vacia(cola):
    return len(cola)==0

def encolar_proc(cola,proc):
    cola.append(proc)

def desencolar_proc(cola):
    aux = cola[0]
    cola.pop(0)
    return aux

def ver_tam(cola):
    return len(cola)

def copiar(cola1,cola2):
    aux = crear_cola()
    while not es_vacia(cola2):
        proc = desencolar_proc(cola2)
        encolar_proc(aux,proc)
    while not es_vacia(aux):
        proc = desencolar_proc(aux)
        encolar_proc(cola1,proc)
        encolar_proc(cola2,proc)
    

