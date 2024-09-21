import random

vehiculos_lista = []
vehiculos_texto = []

#Listas de meses 
Calendario = { 
    "enero": {},
    "febrero": {},
    "marzo": {},
    "abril": {},
    "mayo": {},
    "junio": {},
    "julio": {},
    "agosto": {},
    "septiembre": {},
    "octubre": {},
    "noviembre": {},
    "diciembre": {},
}

#Listas de vehiculos precargada
Autos = [
    toyota:= ["Hilux", "Sw4", "Corolla", "Etios", "Prado"],
    ford:= ["Focus", "Eco-Sport", "Mondeo", "Ranger", "Fiesta", "Fiesta Kinetic"],
    chevrolet:= ["S-10", "Cruze", "Prisma", "Tracker"],
    volkswagen:= ["Gol", "Amarok", "Bora", "Vento", "Passat", "Surán"]
]

#Template de marcas
MarcasNombre = [
    "Toyota",
    "Ford",
    "Chevrolet",
    "Volkswagen"
]

# Asignar 'Características' de cada auto
def preparar_autos(template):
    for modelos in template:
        info_vehiculo = []
        for modelo in modelos:
            ano = random.randint(2000, 2020)
            kms = random.randint(80000, 150000)
            precio = random.randint(2500000, 9000000)
            info_vehiculo.append([modelo, " Año: " + str(ano), "Kms: " + str(kms), "Precio: " + str(precio)])
        vehiculos_texto.append(info_vehiculo)
    
# Crear ventas por mes
def crear_ventas():
    for mes in Calendario:
        for indicemarca in range(len(Autos)):
            marca = Autos[indicemarca]
            nombremarca = MarcasNombre[indicemarca]
            Calendario[mes][nombremarca] = {}
            for indicemodelo in range(len(marca)):
                modelo = Autos[indicemarca][indicemodelo]
                ventas = random.randint(0,6)
                Calendario[mes][nombremarca][modelo] = ventas

#OPCION 1 CONSULTAR VEHÍCULOS DISPONIBLES PARA LA VENTA
def mostrar_disponibles():
    print("_" * 150)
    print("PRECIOS EN PESOS ARGENTINOS ($ARS) \n")
    for indicemarca in range(len(vehiculos_texto)):
        print("Marca:", MarcasNombre[indicemarca])
        print("Autos disponibles:")
        for infoauto in vehiculos_texto[indicemarca]:
            print(str(infoauto).strip("[,]"))
        print("_" * 30)

# FUNCION 2 BUSCAR AUTO DISPONIBLE
def buscar_auto():
    disponible = False
    auto = None
    while auto != "0":
        auto = str(input("Ingrese el modelo que desea buscar (por ejemplo Prado, Gol, Corolla, etc). Ingrese '0' para cancelar. : "))
        for modelos in range(len(vehiculos_lista)):
            for modelo in range(len(vehiculos_lista[modelos])):
                if str.lower(auto) == str.lower(vehiculos_lista[modelos][modelo]):
                    disponible = True
                    info = vehiculos_texto[modelos][modelo]
                    break
        if disponible:
            print("El auto",auto, "se encuentra disponible: \n", str(info).strip("[]"))
        else: 
            print("El auto ingresado no se encuentra disponible")

# FUNCION 3: CONSULTAR VENTAS REALIZADAS POR MES, MODELO Y MARCA
def ultimas_ventas():
    ingresarmes = str.lower(input("Ingrese el mes corriente: "))
    while ingresarmes not in Calendario:
        ingresarmes = str.lower(input("Ingrese un mes válido: "))
    ingresarmarca = str.lower(input("Ingrese una marca: "))
    while ingresarmarca not in MarcasNombre:
        ingresarmarca = str.lower(input("Ingrese una marca válida: "))
    modelo_encontrado = None
    while modelo_encontrado != True:
        if modelo_encontrado == False:
            ingresarmodelo = str.lower(input("Modelo no encontrado, reingrese un modelo: "))
        else:  
            ingresarmodelo = str.lower(input("Ingrese un modelo: "))
        for modelo in Calendario[ingresarmes][ingresarmarca]:
            if str.lower(ingresarmodelo) == str.lower(modelo):
                modelo_encontrado = True
                break
        if modelo_encontrado != True:
            modelo_encontrado = False


    for modelo in Calendario[ingresarmes][ingresarmarca]:
        venta = Calendario[ingresarmes][ingresarmarca][modelo]
        if ingresarmodelo == modelo:
            info_venta = ("Modelo: "+str(modelo)+" - Cantidad de ventas en el mes "+str(ingresarmes)+": "+str(venta))
            print(info_venta)
                     
# OPCION 4: MOSTRAR VENTAS X MES + PROMEDIO
def mostrar_ventas():
    sumaanual = 0
    sumameses = 0
    ingresarmes = str.lower(input("Ingresar el mes actual: "))
    while ingresarmes not in Calendario:
        ingresarmes = str.lower(input("Ingresar un mes válido: "))
    continuar = True
    for mes in Calendario:
        if str.lower(str(mes)) == str.lower(ingresarmes):
            continuar = False
        if not continuar:
            break
        sumamensual = 0
        sumameses += 1
        for marca in Calendario[mes]:
            print("-" * 5)
            print(str(marca + " - Ventas de" + mes))
            print("-" * 5)
            sumamarca = 0
            for modelo in Calendario[mes][marca]:
                venta = Calendario[mes][marca][modelo]
                print(str(modelo)+":"+str(venta))
                sumamarca += venta
                sumamensual += venta
                sumaanual += venta
            print("Total de ventas marca: "+str(marca)+":",sumamarca)
        print("_" * 150)
        print("Total de ventas mes "+str.capitalize(mes)+":",sumamensual)
        print("_" * 150)
    if sumameses <= 0:
        print("No hay suficientes meses.")
        return None
    print("PROMEDIO DE VENTAS POR MES:", (sumaanual/sumameses)) #fix

# "Main" - PREPARAR TODO
def inicializar():
    for marca in Autos:
        vehiculos_lista.append(random.sample(marca, random.randint(1,3)))
    preparar_autos(vehiculos_lista)
    crear_ventas()
    
# MENÚ DE OPCIONES
funciones = {
    "0": None,
    "1": mostrar_disponibles,
    "2": buscar_auto,
    "3": ultimas_ventas,
    "4": mostrar_ventas
}

# PROGRAMA PRINCIPAL
inicializar()

while True:
    opcion = str(input('''
                                    EL PATAGÓNICO AUTOMOTORES
                    
                    Bienvenid@ al menú de inicio de El Patagónico Automotores
                    A continuación se detallan las opciones que el sistema permite realizar:
                    
                    1 - Consultar vehiculos diponibles para la venta
                    2 - Consultar disponibilidad vehículo (Aplicando filtros)
                    3 - Consultar ventas realizadas (por mes; modelo y marca)
                    4 - Consultar ventas (total y promedio de ventas por mes)
                    0 - Cerrar menú
                    
                    Ingrese una opción (número): '''))

    if opcion in funciones:
        opcion = int(opcion)
        if (opcion >= 0 and opcion <= 4) or type(opcion):
            if opcion == 0:
                break
            else:
                funciones[str(opcion)]()
    else:
        print("Opción no válida.")
    