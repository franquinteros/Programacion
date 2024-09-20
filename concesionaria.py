import random

vehiculos_lista = []
vehiculos_texto = []

#Listas de meses 
Calendario = { 
    "Enero": {},
    "Feberero": {},
    "Marzo": {},
    "Abril": {},
    "Mayo": {},
    "Junio": {},
    "Julio": {},
    "Agosto": {},
    "Septiembre": {},
    "Octubre": {},
    "Noviembre": {},
    "Diciembre": {},
}

#Listas de vehiculos precargada
Autos = [
    toyota:= ["Hilux", "Sw4", "Corolla", "Etios", "Prado"],
    ford:= ["Focus", "Eco-Sport", "Mondeo", "Ranger", "Fiesta", "Fiesta Kinetic"],
    chevrolet:= ["S-10", "Cruze", "Prisma", "Tracker"],
    wolkswagen:= ["Gol", "Amarok", "Bora", "Vento", "Passat", "Surán"]
]
#Template de marcas
MarcasNombre = [
    "Toyota",
    "Ford",
    "Chevrolet",
    "Wolkswagen"
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

#FUNCION 2 BUSCAR AUTO DISPONIBLE
def buscar_auto():
    disponible = False
    auto = None
    while auto != "0":
        auto = str(input("Ingrese el modelo que desea buscar (por ejemplo Prado, Gol, Corolla, etc). Ingrese '0' para cancelar. : "))
        for modelos in range(len(vehiculos_lista)):
            for modelo in range(len(vehiculos_lista[modelos])):
                if auto == vehiculos_lista[modelos][modelo][0]:
                    disponible = True
                    info = vehiculos_lista[modelos][modelo]
        if disponible:
            print("El auto",auto, "se encuentra disponible: \n",
                info)
        else: print("El auto ingresado no se encuentra disponible")

#OPCION 4: MOSTRAR VENTAS X MES + PROMEDIO
def mostrar_ventas():
    sumaanual = 0
    for mes in Calendario:
        print(str(mes))
        sumamensual = 0
        for marca in Calendario[mes]:
            print("-" * 5)
            print(str(marca))
            print("-" * 5)
            sumamarca = 0
            for modelo in Calendario[mes][marca]:
                venta = Calendario[mes][marca][modelo]
                print(str(modelo)+":"+str(venta))
                sumamarca += venta
                sumamensual += venta
                sumaanual += venta
            print("TOTAL "+str(marca)+":",sumamarca)
        print("TOTAL "+str(mes)+":",sumamensual)
        print("_" * 150)
    print("PROMEDIO DE VENTAS POR MES:", (sumaanual/12)) #fix

# "Main" - Preparar todo
def inicializar():
    for marca in Autos:
        vehiculos_lista.append(random.sample(marca, random.randint(1,3)))
    vehiculos_texto = preparar_autos(vehiculos_lista)
    crear_ventas()

# MENÚ DE OPCIONES
funciones = {
    "1": mostrar_disponibles,
    "2": buscar_auto,
    "4": mostrar_ventas
}

# PROGRAMA PRINCIPAL
inicializar()

while True:
    opcion = int(input('''
                                    EL PATAGÓNICO AUTOMOTORES
                    
                    Bienvenid@ al menú de inicio de El Patagónico Automotores
                    A continuación se detallan las opciones que el sistema permite realizar:
                    
                    1 - Consultar vehiculos diponibles 
                    2 - Consultar disponibilidad vehículo (Aplicando filtros)
                    3 - Consultar ultimas ventas realizadas
                    4 - Consultar ventas (Total y promedio de cada mes)
                    0 - Cerrar
                    
                    Ingrese una opción (número): '''))
    
    if opcion == 0:
        break
    else:
        funciones[str(opcion)]()
    