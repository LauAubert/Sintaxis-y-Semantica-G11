import os
import TadProceso as tp
import TadCola as tc
import datetime
cola = tc.crear_cola()
cola = [
    [1,'proceso1','x',1,1,datetime.datetime.now()],
    [2,'proceso2','x',2,2,datetime.datetime.now()],
    [3,'proceso3','y',3,3,datetime.datetime.now()],
    [4,'proceso4','y',4,4,datetime.datetime.now()],
    [5,'proceso5','x',5,5,datetime.datetime.now()],
    [6,'proceso6','z',6,6,datetime.datetime.now()],
    [7,'proceso7','y',7,7,datetime.datetime.now()],
    [8,'proceso8','x',8,8,datetime.datetime.now()],
]

print() # Mensaje antes del menu

def limpiarPantalla(): os.system('cls' if os.name=='nt' else 'clear')
def imprimirProc(proc=None):
    if not proc:
        pid = "PID"
        nombre = "Nombre"
        prio = "Prioridad"
        tam = "Tamano"
        tipo = "Tipo"
        fecha = "Fecha"
    else:
        pid = tp.ver_pid(proc)
        nombre = tp.ver_nom(proc)
        prio = tp.ver_prio(proc)
        tam = tp.ver_tam(proc)
        tipo = tp.ver_tipo(proc)
        fecha = tp.ver_fecha(proc)
    print('{:<4}|{:<10}|{:<10}|{:<10}|{:<10}|{:<15}|'.format(
        pid, nombre, prio, tam, tipo, fecha
    ))





def menu():
    invalido = True
    while invalido:
        print('Seleccione una opcion')
        print('1- Encolar proceso')
        print('2- Modificar la prioridad del proceso')
        print('3- Desencolar proceso')
        print('4- Listado de procesos')
        print('5- Dado un determinado mes, modificar la prioridad de los procesos a baja')
        print('6- Eliminar los procesos cuyo tipo sea igual al ingresado')
        print('7- Generar una cola con aquellos procesos cuya última modificación se encuentre entre dos horas dadas')
        try:rta = int(input('->'))
        except: rta = 0
        if rta>7 or rta<1:
            limpiarPantalla()
            print('Opcion invalida, ingrese de nuevo')
        else: return rta 

while True:
    opcion = menu()
    limpiarPantalla()
    if opcion ==1: #Encolar proceso
        proc = tp.crear_proceso()
        print('----ingrese los datos del proceso----')
        print('ingrese ID de proceso')
        pid=int(input('->'))
        print('ingrese nombre')
        nom=input('->')
        print('ingrese prioridad')
        prio=int(input('->'))
        print('ingrese tamano')
        tam=int(input('->'))
        print('ingrese tipo')
        tipo=input('->')
        print('ingrese mes')
        mes=int(input('->'))
        print('ingrese hora')
        hora=int(input('->'))
        tp.cargar_proceso(proc,pid,nom,tipo,tam,prio,mes,hora)
        tc.encolar_proc(cola,proc)

    elif opcion ==2: #Modificar la prioridad del proceso
        print('ingrese el ID del proceso a modificar')
        idbuscado = int(input('->'))
        colaaux = tc.crear_cola()
        while not tc.es_vacia(cola):
            proce = tc.desencolar_proc(cola)
            auxid = tp.ver_pid(proce)
            if(auxid==idbuscado):
                print('ingrese la prioridad nueva')
                tp.mod_prio(proc,int(input('->')))
            tc.encolar_proc(colaaux,proce)
        while not tc.es_vacia(colaaux):
            tc.encolar_proc(cola,tc.desencolar_proc(colaaux))

    elif opcion == 3: #Desencolar proceso
        proc = tc.desencolar_proc(cola)
        print('usted desencoló el proceso con las siguientes propiedades')
        imprimirProc()
        imprimirProc(proc)

    elif opcion == 4: #Listado de procesos
        imprimirProc()
        colaaux = tc.crear_cola()
        while not tc.es_vacia(cola):
            proc = tc.desencolar_proc(cola)
            imprimirProc(proc)
            tc.encolar_proc(colaaux,proc)
        while not tc.es_vacia(colaaux):
            proc = tc.desencolar_proc(colaaux)
            tc.encolar_proc(cola,proc)

    elif opcion == 5: #Dado un determinado mes, modificar la prioridad de los procesos a baja
        print('Ingrese el mes a modificar')
        mes = int(input('->'))
        colaaux = tc.crear_cola()
        while not tc.es_vacia(cola):
            proc = tc.desencolar_proc(cola)
            if mes == tp.ver_mes(proc):
                tp.mod_prio(proc,0)
            tc.encolar_proc(colaaux,proc)
        while not tc.es_vacia(colaaux):
            proc = tc.desencolar_proc(colaaux)
            tc.encolar_proc(cola,proc)


    elif opcion == 6: #Eliminar los procesos cuyo tipo sea igual al ingresado
        print('Ingrese el tipo de proceso a eliminar')
        tipoproc = input('->')
        colaaux = tc.crear_cola()
        while not tc.es_vacia(cola):
            proc = tc.desencolar_proc(cola)
            if tipoproc != tp.ver_tipo(proc):
                tc.encolar_proc(colaaux,proc)
        while not tc.es_vacia(colaaux):
            proc = tc.desencolar_proc(colaaux)
            tc.encolar_proc(cola,proc)
            

    elif opcion == 7: #Generar una cola con aquellos procesos cuya última modificación se encuentre entre dos horas dadas
        print('Ingrese la hora inicial')
        horaini = int(input('->'))
        print('Ingrese la hora final')
        horafin = int(input('->'))
        colaaux = tc.crear_cola()
        colafiltro = tc.crear_cola()
        imprimirProc()
        while not tc.es_vacia(cola):
            proc = tc.desencolar_proc(cola)
            if horaini <= tp.ver_hora(proc) and tp.ver_hora(proc) <= horafin:
                tc.encolar_proc(colafiltro,proc)
                imprimirProc(proc)
            tc.encolar_proc(colaaux,proc)
        while not tc.es_vacia(colaaux):
            proc = tc.desencolar_proc(colaaux)
            tc.encolar_proc(cola,proc)

    if (opcion == 1): limpiarPantalla()

