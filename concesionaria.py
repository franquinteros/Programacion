import random

vehiculos_disponibles = []
imprimir_vehiculos = []

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
AutosNombre = [
    "Toyota",
    "Ford",
    "Chevrolet",
    "Wolkswagen"
]
#Template de meses
MesesNombre = [
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre",
]

# Asignar 'Características' de cada auto
def rellenar_lista(template):
    nuevo = []
    for modelos in template:
        info_vehiculo = []
        for modelo in modelos:
            ano = random.randint(2000, 2020)
            kms = random.randint(80000, 150000)
            precio = random.randint(2500000, 9000000)
            info_vehiculo.append([modelo , " Año: " + str(ano), "Kms: " + str(kms), "Precio: " + str(precio)])
        nuevo.append(info_vehiculo)
    return nuevo

# Asignar autos disponibles
def crear():
    template = []
    for marca in Autos:
        template.append(random.sample(marca, random.randint(1,3)))
    return template   
    
# Crear ventas por mes
def crear_ventas():
    for mes in Calendario:
        for indicemarca in range(len(Autos)):
            marca = Autos[indicemarca]
            nombremarca = AutosNombre[indicemarca]
            Calendario[mes][nombremarca] = {}
            for indicemodelo in range(len(marca)):
                modelo = Autos[indicemarca][indicemodelo]
                ventas = random.randint(0,6)
                Calendario[mes][nombremarca][modelo] = ventas

#OPCION 1 CONSULTAR VEHÍCULOS DISPONIBLES PARA LA VENTA
def mostrar_disponibles():
    print("_" * 150)
    print("PRECIOS EN PESOS ARGENTINOS ($ARS) \n")
    for indicemarca in range(len(imprimir_vehiculos)):
        print("Marca:", AutosNombre[indicemarca])
        print("Autos disponibles:")
        for infoauto in imprimir_vehiculos[indicemarca]:
            print(str(infoauto).strip("[,]"))
        print("_" * 30)

#FUNCION 2 BUSCAR AUTO DISPONIBLE
def buscar_auto(autosDisponibles):
    disponible = 0
    auto = input("Ingrese el modelo que desea buscar (por ejemplo Prado, Gol, Corolla, etc): ")
    for modelos in range(len(autosDisponibles)):
        for modelo in range(len(autosDisponibles[modelos])):
            if auto == autosDisponibles[modelos][modelo][0]:
                disponible = 1
                info = autosDisponibles[modelos][modelo]
    if disponible == 1:
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

#MENÚ DE OPCIONES
funciones = {
    "1": mostrar_disponibles,
    "2": buscar_auto,
    "4": mostrar_ventas
}

#PROGRAMA PRINCIPAL

vehiculos_disponibles = crear() # Eliminar esto en futura versiones
imprimir_vehiculos = rellenar_lista(vehiculos_disponibles)
print(imprimir_vehiculos)
crear_ventas()
print(buscar_auto(imprimir_vehiculos))
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
    