import TadProceso as tp
import TadCola as tc

cola = tc.crear_cola()

print() # Mensaje antes del menu


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
        rta = int(input('->'))
        if rta>7 or rta<1:
            print('Opcion invalida, ingrese de nuevo')
        else: return rta 

while True:
    opcion = menu()
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
        tp.cargar_proceso(proc,pid,nom,tipo,tam,prio)
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
        print('usted desencolo el proceso con las siguientes propiedades')
        print('PID,nombre,prioriodad,tamano,tipo,fecha')
        print(f'{tp.ver_pid(proc)};{tp.ver_nom(proc)};{tp.ver_prio(proc)};{tp.ver_tam(proc)};{tp.ver_tipo(proc)}')

    elif opcion == 4: #Listado de procesos
        print('PID,nombre,prioriodad,tamano,tipo,fecha')
        colaaux = tc.crear_cola()
        while not tc.es_vacia(cola):
            proc = tc.desencolar_proc(cola)
            print(f'{tp.ver_pid(proc)};{tp.ver_nom(proc)};{tp.ver_prio(proc)};{tp.ver_tam(proc)};{tp.ver_tipo(proc)}')
            tc.encolar_proc(colaaux,proc)
        while not tc.es_vacia(colaaux):
            proc = tc.desencolar_proc(colaaux)
            tc.encolar_proc(cola,proc)

    elif opcion == 5: #Dado un determinado mes, modificar la prioridad de los procesos a baja
        pass


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
        pass


