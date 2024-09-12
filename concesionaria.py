import random
#import colorama

lista = []
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

#OPCION 0 CANCELAR 
def cancelar():
    pass

#OPCION 1 CONSULTAR VEHÍCULOS DISPONIBLES PARA LA VENTA
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
            info_vehiculo.append([modelo,"Año:", ano, "Kms:", kms, "Precio:", precio])
        nuevo.append(info_vehiculo)
    return nuevo
def crear():
    template = [
        random.sample(Autos[0], 2),
        random.sample(Autos[1], 2),
        random.sample(Autos[2], 2),
        random.sample(Autos[3], 2)
        ]
    return template

#OPCION 5: MOSTRAR VENTAS X MES
def crear_ventas():
    for indicemes in range(len(Calendario)):
        mes = Calendario[indicemes]
        for indicemarca in range(len(Autos)): 
            marca = Autos[indicemarca] 
            marca_venta = [] 
            for indicemodelo in range(len(marca)):
                modelo = marca[indicemodelo]
                ventas = random.randint(0,6)
                marca_venta.append(ventas)
            mes.append(marca_venta)  
crear_ventas ()

def mostrar_ventas(opcion):
    if opcion == 5:
        for indicemes in range(len(Calendario)):
            total_ventas = []
            mes = Calendario[indicemes]
            meses = "Mes:",MesesNombre[indicemes] #Mes
            print(meses)
            for indicemarca in range(len(mes)):
                marcas = "Marca:",AutosNombre[indicemarca] #Marca
                ventas = mes[indicemarca]
                for indicemodelo in range(len(ventas)):
                    modelos = "Modelo:",Autos[indicemarca][indicemodelo] #Modelo
                    cantidad_ventas = "Ventas:",ventas[indicemodelo] #Ventas
                total_ventas.append([marcas,modelos,cantidad_ventas])
            print(total_ventas,"\n")
    return total_ventas      

def mostrar():
    print("\n- Estos fueron los autos vendidos el último mes.")
    print("_" * 150)
    print(lista)

funciones = [
    cancelar, mostrar
]

#Programa principal
lista = crear()
vehiculos_disponibles = crear() 
imprimir_vehiculos = rellenar_lista(vehiculos_disponibles)
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
    elif opcion == 1:
        print(imprimir_vehiculos) #Falta completar
    elif opcion == 2:
        print(imprimir_vehiculos) #Realizar
    elif opcion == 3:
        print(mostrar_ventas(opcion)) #Realizar
    elif opcion == 4:
        print(mostrar_ventas(opcion)) #Realizar
    elif opcion == 5:
        print(mostrar_ventas(opcion)) #Completo
    