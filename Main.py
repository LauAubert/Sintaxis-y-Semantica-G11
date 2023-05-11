import os
import sys
import TadProceso as tp
import TadCola as tc
import random


cola = tc.crear_cola()
tiposPrueba = ['x','y','z'] # genero una lista de tipos de prueba
for i in range(10): # genero 10 procesos de prueba
    proc = tp.crear_proceso() 
    tp.cargar_proceso( # cargo los datos del proceso al azar
        proc,
        pid=i,
        nom="nom"+str(i),
        tipo=tiposPrueba[random.randint(0,2)], # elijo un tipo al azar de la lista
        tam=random.randint(1,100),
        prio=random.randint(1,3),
        mes=random.randint(1,12),
        hora=random.randint(0,23),
        minutos=random.randint(0,59)
    )
    tc.encolar_proc(cola,proc) # encolo el proceso aleatorio en la cola



def limpiarPantalla(): os.system('cls' if os.name=='nt' else 'clear')

def imprimirProc(proc=None): #Funcion que sirve para mostrar los procesos en forma de tabla
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

def ingresarValor(min:int=0,max:int=0):
    # Funcion para ingresar un valor entero por teclado en un rango especifico
    while True:
        try:
            valor = int(input('->')) # Leo el valor ingresado
            if min==0 and max==0: return valor # Si no se especifica rango y es INT devuelvo el valor
            if valor<min or valor>max: raise Exception # Si el valor no esta en el rango lanzo una excepcion
            return valor
        except: # Si el valor no es INT o no esta en el rango muestro un mensaje de error
            sys.stdout.write('\x1b[1A' + '\x1b[2K') # Borro la linea anterior
            print('Valor invalido, ingrese de nuevo') 


#test
def menu(): #Creamos una funcion que es para hacer uso del menu
    
    while True:
        print('Seleccione una opcion')
        print('0- Salir')
        print('1- Encolar proceso')
        print('2- Modificar la prioridad del proceso')
        print('3- Desencolar proceso')
        print('4- Listado de procesos')
        print('5- Dado un determinado mes, modificar la prioridad de los procesos a baja')
        print('6- Eliminar los procesos cuyo tipo sea igual al ingresado')
        print('7- Generar una cola con aquellos procesos cuya última modificación se encuentre entre dos horas dadas')
        try:rta = int(input('->')) #Intenta ingresar una respuesta y convertirla a entero
        except: rta = 8 #Si la respuesta no es entera, rta=8
        if rta==0: exit() #Si la respuesta es 0, sale del programa
        if rta>7 or rta<1: #Una vez que se ingresa el valor de la respuesta, se hace la comprobacion de si esta entre 1 y 7
            limpiarPantalla()
            print('Opcion invalida, ingrese de nuevo') #Si la respuesta esta fuera del rango limpia la pantalla e imprime que la opcion no es valida 
        else: return rta #Si la respuesta esta en el rango la devuelve

while True:
    opcion = menu() #Se usa la funcion menu para obtener el valor de la respuesta
    limpiarPantalla() 
    if opcion ==1: #Encolar proceso
        proc = tp.crear_proceso() #Crea un proceso vacio
        print('----ingrese los datos del proceso----')
        print('ingrese ID de proceso')
        pid=ingresarValor()
        print('ingrese nombre')
        nom=input('->')
        print('ingrese prioridad')
        prio=ingresarValor()
        print('ingrese tamano')
        tam=ingresarValor()
        print('ingrese tipo')
        tipo=input('->')
        print('ingrese mes')
        mes=ingresarValor(1,12)
        print('ingrese hora')
        hora=ingresarValor(0,23)
        print('ingrese minutos')
        minutos=ingresarValor(0,59)
        tp.cargar_proceso(proc,pid,nom,tipo,tam,prio,mes,hora,minutos) #Con los datos ingresados, carga el proceso y lo encola
        tc.encolar_proc(cola,proc)

    elif opcion ==2: #Modificar la prioridad del proceso
        print('ingrese el ID del proceso a modificar')
        idbuscado = ingresarValor() #Ingresa un id para buscar el proceso
        colaaux = tc.crear_cola() #Crea una cola vacia auxiliar
        while not tc.es_vacia(cola):  #Mientras la cola no es vacia, desencola el primer proceso y guarda el pid del mismo en auxid
            proc = tc.desencolar_proc(cola)
            auxid = tp.ver_pid(proc)
            if(auxid==idbuscado): #! PONER UN FLAG SI FUE ENCONTRADO O NO
                print('ingrese la prioridad nueva')
                tp.mod_prio(proc,ingresarValor())
            tc.encolar_proc(colaaux,proc)  #Busca el id y encola los procesos en una cola auxiliar, si lo encuentra lo modifica y lo encola en aux de la misma manera
        while not tc.es_vacia(colaaux):
            tc.encolar_proc(cola,tc.desencolar_proc(colaaux)) #Se encolan los procesos nuevamente en la cola original y el proceso buscado con la prioridad modificada

    elif opcion == 3: #Desencolar proceso
        proc = tc.desencolar_proc(cola) 
        print('usted desencoló el proceso con las siguientes propiedades')
        imprimirProc() #Muestra la tabla
        imprimirProc(proc) #Muestra el proceso desencolado
        input('presione enter para continuar')

    elif opcion == 4: #Listado de procesos
        imprimirProc()
        colaaux = tc.crear_cola()    
        while not tc.es_vacia(cola):        #Mientras la cola no este vacia, desencola uno por uno los procesos, los imprime con el formato de la funcion imprimirProc y los encola en la colaaux
            proc = tc.desencolar_proc(cola)
            imprimirProc(proc)
            tc.encolar_proc(colaaux,proc)
        while not tc.es_vacia(colaaux):   #Vuelve a encolar los procesos en la cola original
            proc = tc.desencolar_proc(colaaux)
            tc.encolar_proc(cola,proc)
        input('presione enter para continuar')

    elif opcion == 5: #Dado un determinado mes, modificar la prioridad de los procesos a baja
        print('Ingrese el mes a modificar') 
        mes = ingresarValor(1,12)    
        colaaux = tc.crear_cola()  
        while not tc.es_vacia(cola):   #Desencola cada proceso
            proc = tc.desencolar_proc(cola)
            if mes == tp.ver_mes(proc): #Verifica que el mes sea igual al ingresado, y les cambia la prioridad
                tp.mod_prio(proc,0)
            tc.encolar_proc(colaaux,proc) #Encola todos los procesos, incluidos los modificados en colaaux
        while not tc.es_vacia(colaaux): #Devuelve los procesos a la cola original
            proc = tc.desencolar_proc(colaaux)
            tc.encolar_proc(cola,proc)
        print('Se modificaron los procesos del mes',mes,'a prioridad baja')
        input('presione enter para continuar')


    elif opcion == 6: #Eliminar los procesos cuyo tipo sea igual al ingresado
        print('Ingrese el tipo de proceso a eliminar')
        tipoproc = input('->')   
        colaaux = tc.crear_cola()
        while not tc.es_vacia(cola):   #Mientras la cola no es vacia
            proc = tc.desencolar_proc(cola) #Desencola cada proceso
            if tipoproc != tp.ver_tipo(proc): #Si el tipo ingresado es igual al del proceso, lo borra y sino lo encola en la colaaux
                tc.encolar_proc(colaaux,proc)
        while not tc.es_vacia(colaaux): #Devuelve los procesos, sin los que fueron eliminados, a la cola original
            proc = tc.desencolar_proc(colaaux)
            tc.encolar_proc(cola,proc)
        print('Se eliminaron los procesos de tipo',tipoproc) 
        input('presione enter para continuar')
            

    elif opcion == 7: #Generar una cola con aquellos procesos cuya última modificación se encuentre entre dos horas dadas
        print('Ingrese la hora inicial')     #Se ingresa el rango de tiempo de los procesos que se estan buscando
        horaini = ingresarValor(0,23)
        print('Ingrese los minutos iniciales')
        minini = ingresarValor(0,59)
        print('Ingrese la hora final')
        horafin = ingresarValor(0,23)
        print('Ingrese los minutos finales')
        minfin = ingresarValor(0,59)
        colaaux = tc.crear_cola()
        colafiltro = tc.crear_cola()
        imprimirProc()
        while not tc.es_vacia(cola):            #Mientras la cola no es vacia, desencola los procesos, convierte las horas y minutos en enteros (ingresadas y de los procesos desencolados)
            proc = tc.desencolar_proc(cola)
            if ((horaini*100+minini <= tp.ver_hora(proc)*100+tp.ver_min(proc)) 
                and (tp.ver_hora(proc)*100+tp.ver_min(proc) <= horafin*100+minfin)):
                tc.encolar_proc(colafiltro,proc)    #Los compara en la condicion del if y si estan dentro de las horas dadas, los encola en la colafiltro y los imprime
                imprimirProc(proc)
            tc.encolar_proc(colaaux,proc)  #Tambien los encola en la colaaux
        while not tc.es_vacia(colaaux):  #Devuelve los procesos a la cola original
            proc = tc.desencolar_proc(colaaux)
            tc.encolar_proc(cola,proc)
        input('presione enter para continuar')

    limpiarPantalla()

