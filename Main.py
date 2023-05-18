import os # importo OS para la funcion limpiarPantalla()
import sys # importo SYS para la funcion ingresarValor() (borrar linea anterior)
import TadProceso as tp 
import TadCola as tc
import random # importo RANDOM para generar datos aleatorios de prueba
import mensaje # importo el modulo mensaje para mostrar el mensaje de bienvenida (ASCII ART)


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
        ano=random.randint(2019,2020),
        mes=random.randint(1,12),
        dia=random.randint(25,28),
        hora=random.randint(0,23),
        minutos=random.randint(0,59)
    )
    tc.encolar_proc(cola,proc) # encolo el proceso aleatorio en la cola



def limpiarPantalla(): os.system('cls' if os.name=='nt' else 'clear')
def imprimirProc(proc=None):
    '''Si se la llama sin parámetro imprime la cabecera de la tabla, si se le pasa un proceso imprime los datos del proceso como una fila de la tabla'''
    listaPrio = ['','Baja','Media','Alta']
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
        prio = listaPrio[tp.ver_prio(proc)] # obtengo la prioridad del proceso y la convierto en string para mostrarla
        tam = tp.ver_tam(proc)
        tipo = tp.ver_tipo(proc)
        fecha = tp.ver_fecha(proc)
    print('{:<4}|{:<10}|{:<10}|{:<10}|{:<10}|{:<16}|'.format(
        pid, nombre, prio, tam, tipo, fecha
    ))

def ingresarValor(min:int=0,max:int=0):
    '''Retorna un valor entero ingresado por el usuario, si se especifica un rango, el valor debe estar dentro de ese rango'''
    while True:
        try:
            valor = int(input('->')) # Leo el valor ingresado
            if min==0 and max==0: return valor # Si no se especifica rango y es INT devuelvo el valor
            if valor<min or valor>max: raise Exception # Si el valor no esta en el rango lanzo una excepcion
            return valor
        except: # Si el valor no es INT o no esta en el rango muestro un mensaje de error
            sys.stdout.write('\x1b[1A' + '\x1b[2K') # Borro la linea anterior
            print('Valor invalido, ingrese de nuevo') 


mensaje.mensaje()
input()
limpiarPantalla()
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
        idcorr = True
        while(idcorr):
            print('ingrese ID de proceso')
            pid=ingresarValor()
            colaaux1 = tc.crear_cola()
            tc.copiar(colaaux1,cola)
            while not tc.es_vacia(colaaux1):
                procaux1 = tc.desencolar_proc(colaaux1)
                pidaux = tp.ver_pid(procaux1)
                if pidaux == pid:
                    print("error , este id de proceso ya existe")
                    break
            if pidaux != pid:
                idcorr = False

        print('ingrese nombre')
        nom=input('->')
        print('ingrese prioridad \n  1-Baja \n  2-Media \n  3-Alta')
        prio=ingresarValor(1,3)
        print('ingrese tamaño')
        tam=ingresarValor()
        print('ingrese tipo')
        tipo=input('->')
        print('ingrese año')
        ano=ingresarValor(1,2023)
        print('ingrese mes')
        mes=ingresarValor(1,12)
        print('ingrese dia')
        diasmes=[31,28,31,30,31,30,31,31,30,31,30,31]
        dia=ingresarValor(1,diasmes[mes-1])
        print('ingrese hora')
        hora=ingresarValor(0,23)
        print('ingrese minutos')
        minutos=ingresarValor(0,59)
        tp.cargar_proceso(proc,pid,nom,tipo,tam,prio,ano,mes,dia,hora,minutos) #Con los datos ingresados, carga el proceso y lo encola
        tc.encolar_proc(cola,proc)

    elif opcion ==2: #Modificar la prioridad del proceso
        print('ingrese el ID del proceso a modificar')
        idbuscado = ingresarValor() #Ingresa un id para buscar el proceso
        colaaux = tc.crear_cola() #Crea una cola vacia auxiliar
        flag = False
        while not tc.es_vacia(cola):  #Mientras la cola no es vacia, desencola el primer proceso y guarda el pid del mismo en auxid
            proc = tc.desencolar_proc(cola)
            auxid = tp.ver_pid(proc)
            if(auxid==idbuscado):
                flag = True 
                print('ingrese prioridad \n  1-Baja \n  2-Media \n  3-Alta')
                prio=ingresarValor(1,3)
                tp.mod_prio(proc,prio) 
                print('Se modificó la prioridad del proceso con el ID ingresado')
                imprimirProc()
                imprimirProc(proc) 
            tc.encolar_proc(colaaux,proc)  #Busca el id y encola los procesos en una cola auxiliar, si lo encuentra lo modifica y lo encola en aux de la misma manera
        while not tc.es_vacia(colaaux):
            tc.encolar_proc(cola,tc.desencolar_proc(colaaux)) #Se encolan los procesos nuevamente en la cola original y el proceso buscado con la prioridad modificada
        if flag == False: print('No se encontró el proceso con el ID ingresado') #Si no se encuentra el proceso, se imprime un mensaje de error
        input('presione enter para continuar')

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
        limpiarPantalla()
        colaaux = tc.crear_cola()  
        flag = False
        while not tc.es_vacia(cola):   #Desencola cada proceso
            proc = tc.desencolar_proc(cola)
            if mes == tp.ver_mes(proc): #Verifica que el mes sea igual al ingresado, y les cambia la prioridad
                if flag == False: imprimirProc()
                flag = True
                tp.mod_prio(proc,1)
                imprimirProc(proc)
            tc.encolar_proc(colaaux,proc) #Encola todos los procesos, incluidos los modificados en colaaux
        while not tc.es_vacia(colaaux): #Devuelve los procesos a la cola original
            proc = tc.desencolar_proc(colaaux)
            tc.encolar_proc(cola,proc)
        if flag == False: print('No se encontraron procesos con el mes ingresado')
        else: print('Se modificaron los procesos del mes',mes,'a prioridad baja')
        input('presione enter para continuar')


    elif opcion == 6: #Eliminar los procesos cuyo tipo sea igual al ingresado
        print('Ingrese el tipo de proceso a eliminar')
        tipoproc = input('->')   
        colaaux = tc.crear_cola()
        limpiarPantalla()
        flag = False
        while not tc.es_vacia(cola):   #Mientras la cola no es vacia
            proc = tc.desencolar_proc(cola) #Desencola cada proceso
            if tipoproc != tp.ver_tipo(proc): #Si el tipo ingresado es igual al del proceso, lo borra y sino lo encola en la colaaux
                tc.encolar_proc(colaaux,proc)
            else: 
                if flag == False:imprimirProc()
                flag = True 
                imprimirProc(proc) #Si el tipo es igual, lo imprime
        while not tc.es_vacia(colaaux): #Devuelve los procesos, sin los que fueron eliminados, a la cola original
            proc = tc.desencolar_proc(colaaux)
            tc.encolar_proc(cola,proc)
        if flag == False: print('No se encontraron procesos con el tipo ingresado')
        else: print('Se listan los procesos eliminados con el tipo',tipoproc)
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
        limpiarPantalla()
        flag = False
        while not tc.es_vacia(cola):            #Mientras la cola no es vacia, desencola los procesos, convierte las horas y minutos en enteros (ingresadas y de los procesos desencolados)
            proc = tc.desencolar_proc(cola)
            if ((horaini*100+minini <= tp.ver_hora(proc)*100+tp.ver_min(proc)) 
                and (tp.ver_hora(proc)*100+tp.ver_min(proc) <= horafin*100+minfin)):
                if flag == False: imprimirProc()
                flag = True
                tc.encolar_proc(colafiltro,proc)    #Los compara en la condicion del if y si estan dentro de las horas dadas, los encola en la colafiltro y los imprime
                imprimirProc(proc)
            tc.encolar_proc(colaaux,proc)  #Tambien los encola en la colaaux
        while not tc.es_vacia(colaaux):  #Devuelve los procesos a la cola original
            proc = tc.desencolar_proc(colaaux)
            tc.encolar_proc(cola,proc)
        if not flag: print('No se encontraron procesos con la hora ingresada')
        input('presione enter para continuar')

    limpiarPantalla()