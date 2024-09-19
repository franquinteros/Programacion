import random

vehiculos_disponibles = []
imprimir_vehiculos = []

#Listas de meses 
Calendario = [ # 0 al 11
    Enero:= [],
    Febrero:= [],
    Marzo:= [],
    Abril:= [],
    Mayo:= [],
    Junio:= [],
    Julio:= [],
    Agosto:= [],
    Septiembre:= [],
    Octubre:= [],
    Noviembre:= [],
    Diciembre:= [],
]
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
        '''for marca in AutosNombre:
        info_vehiculo.append(marca)'''
        for modelo in modelos:
            ano = random.randint(2000, 2020)
            kms = random.randint(80000, 150000)
            precio = random.randint(2500000, 9000000)
            info_vehiculo.append([modelo + " Año: " + str(ano), "Kms: " + str(kms), "Precio: " + str(precio)])
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
    for indicemes in range(len(Calendario)):
        mes = Calendario[indicemes]
        for indicemarca in range(len(Autos)): 
            marca = Autos[indicemarca] 
            marca_venta = [] 
            for indicemodelo in range(len(marca)):
                ventas = random.randint(0,6)
                marca_venta.append(ventas)
            mes.append(marca_venta)

#OPCION 0 CANCELAR 
def cancelar():
    pass

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

#OPCION 5: MOSTRAR VENTAS X MES

def mostrar_ventas(opcion):
    if opcion == 5:
        for indicemes in range(len(Calendario)):
            ventasmes = []
            mes = Calendario[indicemes] # Lista del calendario mes (Enero = [])
            mestexto = "Mes:",MesesNombre[indicemes] #Mes nombre
            print(mestexto)
            for indicemarca in range(len(mes)):
                ventamarca = mes[indicemarca] # Lista de la marca [3,3,4,4,5]
                marcatexto = "Marca:",AutosNombre[indicemarca] # Marca nombre
                print(marcatexto)
                ventasmarca = []
                for indicemodelo in range(len(Autos[indicemarca])):
                    modelonombre = "Modelo:", Autos[indicemarca][indicemodelo]
                    ventavalor = ventamarca[indicemodelo]
                    ventasmarca.append([modelonombre, ventavalor])
                ventasmes.append(ventasmarca)
                print(ventasmarca)

funciones = [
    cancelar, mostrar_disponibles
]

#Programa principal
vehiculos_disponibles = crear() # Eliminar esto en futura versiones
imprimir_vehiculos = rellenar_lista(vehiculos_disponibles)
crear_ventas()

while True:
    opcion = int(input('''
                                    EL PATAGÓNICO AUTOMOTORES
                    
                    Bienvenid@ al menú de inicio de El Patagónico Automotores
                    A continuación se detallan las opciones que el sistema permite realizar:
                    
                    1 - Consultar vehiculos diponibles 
                    2 - Consultar promedio de ventas por mes
                    3 - Consultar disponibilidad vehículo (Aplicando filtros)
                    4 - Consultar ultimas ventas realizadas
                    5 - Consultar ventas realizadas mes a mes 
                    0 - Cerrar
                    
                    Ingrese una opción (número): '''))
    if opcion == 0:
        break
    elif opcion == 2:
        print(imprimir_vehiculos) #Realizar
    elif opcion == 3:
        print(mostrar_ventas(opcion)) #Realizar
    elif opcion == 4:
        print(mostrar_ventas(opcion)) #Realizar
    elif opcion == 5:
        print(mostrar_ventas(opcion)) #Completo
    else:
        funciones[opcion]()
    