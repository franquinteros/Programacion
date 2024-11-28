
import json

#FUNCION 1
#Mostrar los vehiculos que se encuentran disponibles
def mostrar_info_json(arch="/Users/franciscoquinteros/Documents/UADE/Programación/UADE 24/2do cuatr/TPO/archivos/disponibles.json"):
    try:
        file = open(arch, "r", encoding="utf-8")
        try:
            datos = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            datos = []
        finally:
            file.close()
        
        if not datos:
            print("No hay vehículos disponibles.")
            return
        
        headers = ["Marca", "Modelo", "Año", "Kilómetros", "Precio"]
        
        #Titulos
        print(f"{'Marca':<15}{'Modelo':<15}{'Año':<6}{'Kilómetros':<12}{'Precio':<12}")
        print("-" * 60) 
        
        #Imprime la información de los vehículos en formato filas y columnas
        for auto in datos:
            print(f"{auto['marca']:<15}{auto['modelo']:<15}{auto['año']:<6}{auto['kilometros']:<12}{auto['precio']:<12}")
    
    except Exception as e:
        print(f"Ocurrió un error al mostrar la información: {e}")
        
#FUNCION PARA SOLICITAR INFO DEL VEHICULO AL USUARIO 
def obtener_info_vehiculo():

        #Valida la marca
        while True:
            marca = input("Ingrese la marca del vehículo: ").strip()
            if not marca:
                print("La marca no puede estar vacía. Inténtelo nuevamente.")
                continue
            break 
        
        #Valida el modelo
        while True:
            modelo = input("Ingrese el modelo del vehículo: ").strip()
            if not modelo:
                print("El modelo no puede estar vacío. Inténtelo nuevamente.")
                continue
            break
        
        #Valida el año
        while True:
            año = input("Ingrese el año del vehículo: ").strip()
            if not año.isdigit():
                print("El año debe ser un número válido. Inténtelo nuevamente.")
                continue
            año = int(año)
            break 
        
        #Valida los kilómetros
        while True:
            kilometros = input("Ingrese los kilómetros del vehículo: ").strip()
            if not kilometros.replace(".", "", 1).isdigit():
                print("Los kilómetros deben ser un número válido. Inténtelo nuevamente.")
                continue
            kilometros = float(kilometros)
            break
        
        #Valida el precio
        while True:
            precio = input("Ingrese el precio del vehículo: ").strip()
            if not precio.replace(".", "", 1).isdigit():
                print("El precio debe ser un número válido. Inténtelo nuevamente.")
                continue
            precio = float(precio)
            break

        return {
            "marca": marca,
            "modelo": modelo,
            "año": año,
            "kilometros": kilometros,
            "precio": precio
        }

#FUNCION 2 
#Guardar la información en el archivo JSON
def guardar_info_json(vehiculo, arch="/Users/franciscoquinteros/Documents/UADE/Programación/UADE 24/2do cuatr/TPO/archivos/disponibles.json"):
    try:
        file =  open(arch, "r", encoding="utf-8")
        try:
            datos = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            datos = [] 
        file.close()
        
        datos.append(vehiculo)  #Agrega el vehículo a la lista de datos
        
        #Guardar la lista actualizada en el archivo
        file = open(arch, "w", encoding="utf-8")
        json.dump(datos, file, indent=4, ensure_ascii=False)
        file.close()
        print(f"Información del vehículo guardada con éxito.")
        
    except Exception as e:
        print(f"Ocurrió un error al guardar la información: {e}")

#FUNCION PARA VALIDAR FECHAS
def validar_fecha(fecha):
    partes = fecha.split("/")
    if len(partes) != 3:
        return False  

    try:
        dia, mes, año = map(int, partes)
    except ValueError:
        return False  

    if mes < 1 or mes > 12:
        return False
    
    dias_por_mes = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    #Para años bisiestos
    if mes == 2 and (año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)):
        dias_por_mes[2] = 29

    if dia < 1 or dia > dias_por_mes[mes]:
        return False

    return True

#FUNCION 3
#Marcar vehículo como vendido
def marcar_auto_vendido(vehiculo, arch_disponibles="/Users/franciscoquinteros/Documents/UADE/Programación/UADE 24/2do cuatr/TPO/archivos/disponibles.json", arch_vendidos="/Users/franciscoquinteros/Documents/UADE/Programación/UADE 24/2do cuatr/TPO/archivos/vendidos.json"):
    try:
        file = open(arch_disponibles, "r", encoding="utf-8")
        try:
            autos_disponibles = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            autos_disponibles = []
        finally:
            file.close()
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo de disponibles: {e}")
        autos_disponibles = []
    
    #Buscar el vehículo en los disponibles y eliminarlo
    for auto in autos_disponibles:
        if auto["marca"] == vehiculo["marca"] and auto["modelo"] == vehiculo["modelo"] and auto["año"] == vehiculo["año"]:
            autos_disponibles.remove(auto)
            break
    else:
        print("El vehículo no se encontró en los disponibles.")
        return

    #Guardar los vehículos restantes en el archivo de disponibles
    file = open(arch_disponibles, "w", encoding="utf-8")
    json.dump(autos_disponibles, file, indent=4, ensure_ascii=False)
    file.close()

    #Obtener los datos de venta
    while True:
        fecha_venta = input("Ingrese la fecha de venta (DD/MM/AA): ")
        vendedor = input("Ingrese su nombre y apellido: ")
        if validar_fecha(fecha_venta):
            break
        print("Fecha no válida. Inténtelo de nuevo.")
    
    #Crea el diccionario con los datos del vehículo y la venta
    vehiculo_vendido = {
        "marca": vehiculo["marca"],
        "modelo": vehiculo["modelo"],
        "año": vehiculo["año"],
        "kilometros": vehiculo["kilometros"],
        "precio": vehiculo["precio"],
        "fecha venta": fecha_venta,
        "vendedor": vendedor
    }

    #Leer archivo de vehículos vendidos
    try:
        file = open(arch_vendidos, "r", encoding="utf-8")
        try:
            datos_vendidos = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            datos_vendidos = []
        finally:
            file.close()
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo de vendidos: {e}")
        datos_vendidos = []

    #Agregar el vehículo vendido
    datos_vendidos.append(vehiculo_vendido)

    #Guardar la lista de vehículos vendidos actualizada
    file = open(arch_vendidos, "w", encoding="utf-8")
    json.dump(datos_vendidos, file, indent=4, ensure_ascii=False)
    file.close()

    print(f"Información del vehículo marcado como vendido y guardada con éxito en el listado de vendidos.")

#FUNCION 4
#Ventas por mes (promedio, marca más vendida, modelo más vendido, total ingresos, y vendedor con más ventas)
def mostrar_ventas_mes(arch_vendidos="/Users/franciscoquinteros/Documents/UADE/Programación/UADE 24/2do cuatr/TPO/archivos/vendidos.json"):
    try:
        file = open(arch_vendidos, "r", encoding="utf-8")
        datos_vendidos = json.load(file)
        file.close()
        
        if not datos_vendidos:
            print("No hay ventas registradas.")
            return
        
        #Variables para acumular los resultados
        ventas_por_mes = {}
        ingresos_totales = 0
        ingresos_por_mes = {} 
        marcas = {}
        modelos = {}
        vendedores = {} 
        
        for venta in datos_vendidos:
            fecha_venta = venta["fecha venta"]
            dia, mes, año = fecha_venta.split("/")

            mes_venta = mes + "/" + año 
            
            #Contar las ventas por mes
            if mes_venta not in ventas_por_mes:
                ventas_por_mes[mes_venta] = 0
            ventas_por_mes[mes_venta] += 1
            
            #Acumular ingresos por mes
            if mes_venta not in ingresos_por_mes:
                ingresos_por_mes[mes_venta] = 0
            ingresos_por_mes[mes_venta] += venta["precio"]
            
            #Acumular ingresos totales
            ingresos_totales += venta["precio"]
            
            #Contar marcas y modelos más vendidos
            marca = venta["marca"].lower() 
            modelo = venta["modelo"].lower()
            
            if marca not in marcas:
                marcas[marca] = 0
            marcas[marca] += 1
            
            if modelo not in modelos:
                modelos[modelo] = 0
            modelos[modelo] += 1
            
            #Contar ventas por vendedor
            vendedor = venta["vendedor"].lower()
            if vendedor not in vendedores:
                vendedores[vendedor] = 0
            vendedores[vendedor] += 1
        
        #Marca más vendida
        marca_mas_vendida = max(marcas, key=marcas.get)
        cantidad_marca_mas_vendida = marcas.get(marca_mas_vendida, 0)
        
        #Modelo más vendido
        modelo_mas_vendido = max(modelos, key=modelos.get)
        cantidad_modelo_mas_vendido = modelos.get(modelo_mas_vendido, 0)
        
        #Vendedor con más ventas
        vendedor_mas_exitoso = max(vendedores, key=vendedores.get)
        cantidad_ventas_vendedor = vendedores.get(vendedor_mas_exitoso, 0)
        
        #Mostrar resultados generales
        print(f"Total de ingresos: ${ingresos_totales:,.2f}")
        print(f"Marca más vendida: {marca_mas_vendida.capitalize()} con {cantidad_marca_mas_vendida} ventas")
        print(f"Modelo más vendido: {modelo_mas_vendido.capitalize()} con {cantidad_modelo_mas_vendido} ventas")
        print(f"Vendedor con más ventas: {vendedor_mas_exitoso.title()} con {cantidad_ventas_vendedor} ventas")
        
        #Mostrar ingresos por mes
        print("\nIngresos por mes:")
        for mes, ingresos in ingresos_por_mes.items():
            print(f"{mes}: ${ingresos:,.2f}")
        
        #Mostrar ventas por mes
        print("\nVentas por mes:")
        for mes, ventas in ventas_por_mes.items():
            print(f"{mes}: {ventas} ventas")
        
    except Exception as e:
        print(f"Ocurrió un error al procesar las ventas: {e}")      
          
#FUNCION 5
#Para buscar autos disponibles según criterios
def buscar_autos_disponibles(criterios=None, arch="/Users/franciscoquinteros/Documents/UADE/Programación/UADE 24/2do cuatr/TPO/archivos/disponibles.json"):
    
    if criterios is None:
        criterios = {}

    try:
        with open(arch, "r", encoding="utf-8") as file:
            autos_disponibles = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No se pudo leer el archivo o está vacío.")
        return

    if not autos_disponibles:
        print("No hay vehículos disponibles para mostrar.")
        return

    #Filtrar autos según los criterios proporcionados
    autos_filtrados = []
    for auto in autos_disponibles:
        coincidencia = True
        for key, value in criterios.items():
            if str(auto.get(key, "")).lower() != str(value).lower():
                coincidencia = False
                break
        if coincidencia:
            autos_filtrados.append(auto)

    #Mostrar los resultados
    if not autos_filtrados:
        print("No se encontraron vehículos que coincidan con los criterios.")
    else:
        print(f"{'Marca':<15}{'Modelo':<15}{'Año':<6}{'Kilómetros':<12}{'Precio':<12}")
        print("-" * 60)
        for auto in autos_filtrados:
            print(f"{auto['marca']:<15}{auto['modelo']:<15}{auto['año']:<6}{auto['kilometros']:<12}{auto['precio']:<12}")

#FUNCION 6 
#Para buscar autos disponibles por rango de precios
def buscar_autos_por_rango_precio(arch="/Users/franciscoquinteros/Documents/UADE/Programación/UADE 24/2do cuatr/TPO/archivos/disponibles.json"):
    try:
        with open(arch, "r", encoding="utf-8") as file:
            autos_disponibles = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No se pudo leer el archivo o está vacío.")
        return

    if not autos_disponibles:
        print("No hay vehículos disponibles para mostrar.")
        return

    #Solicita el rango de precios al usuario con validación
    while True:
        try:
            precio_min_input = input("Ingrese el precio mínimo del vehículo (deje en blanco para omitir): ").strip()
            precio_min = float(precio_min_input) if precio_min_input else None
        except ValueError:
            precio_min = None  

        try:
            precio_max_input = input("Ingrese el precio máximo del vehículo (deje en blanco para omitir): ").strip()
            precio_max = float(precio_max_input) if precio_max_input else None
        except ValueError:
            precio_max = None 

        #Verifica que el precio mínimo no sea mayor que el máximo
        if precio_min is not None and precio_max is not None and precio_min > precio_max:
            print("El precio mínimo no puede ser mayor que el precio máximo. Por favor, intente nuevamente.")
        else:
            break 

    #Filtra los autos dentro del rango de precios, si es proporcionado
    autos_filtrados = []
    for auto in autos_disponibles:
        precio = auto.get("precio")
        if precio_min is not None and precio < precio_min:
            continue
        if precio_max is not None and precio > precio_max:
            continue
        autos_filtrados.append(auto)

    #Muestra los resultados
    if not autos_filtrados:
        print("No se encontraron vehículos que coincidan con el rango de precios.")
    else:
        print(f"{'Marca':<15}{'Modelo':<15}{'Año':<6}{'Kilómetros':<12}{'Precio':<12}")
        print("-" * 60)
        for auto in autos_filtrados:
            print(f"{auto['marca']:<15}{auto['modelo']:<15}{auto['año']:<6}{auto['kilometros']:<12}{auto['precio']:<12}")

#MENÚ PRINCIPAL
def mostrar_menu():
    print("=" * 50)
    print(" " * 10 + "EL PATAGÓNICO AUTOMOTORES")
    print("=" * 50)
    print("""
    Bienvenid@ al menú principal.
    A continuación, seleccione una de las opciones:

    1. Mostrar vehículos disponibles para la venta
    2. Ingresar nuevo vehículo 
    3. Marcar vehículo como vendido
    4. Mostrar ventas por mes
    5. Buscar auto
    6. Buscar auto por rango de precios
    0. Cerrar menú
    """)
    print("=" * 50)

def menu():
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción (0-6): ").strip()

        if opcion.isdigit():
            opcion = int(opcion)
            if opcion == 1:
                print("=" * 50)
                print("VEHÍCULOS DISPONIBLES")
                mostrar_info_json()
            elif opcion == 2:
                print("=" * 50)
                print("AGREGAR VEHÍCULO")
                vehiculo = obtener_info_vehiculo()
                guardar_info_json(vehiculo)
            elif opcion == 3:
                print("=" * 50)
                print("MARCAR VEHÍCULO VENDIDO")
                vehiculo = obtener_info_vehiculo()
                marcar_auto_vendido(vehiculo)
            elif opcion == 4:
                print("=" * 50)
                print("MOSTRAR DATOS DE VENTAS POR MES")
                mostrar_ventas_mes()
            elif opcion == 5:
                print("=" * 50)
                print("BUSCAR AUTO DISPONIBLE")
                print("Ingrese los criterios de búsqueda (deje en blanco para omitir):")
                marca = input("Marca: ").strip()
                modelo = input("Modelo: ").strip()
                año = input("Año: ").strip()
                criterios = {}
                if marca:
                    criterios["marca"] = marca
                if modelo:
                    criterios["modelo"] = modelo
                if año:
                    criterios["año"] = int(año)
                buscar_autos_disponibles(criterios)
            elif opcion == 6:
                print("=" * 50)
                print("BUSCAR AUTO POR RANGO DE PRECIOS")
                buscar_autos_por_rango_precio()
            elif opcion == 0:
                print("\nAUTOMOTORES EL PATAGÓNICO / Saliendo del programa...")
                break
            else:
                print("\nPor favor, ingrese un número entre 0 y 5.")
        else:
            print("\nEntrada inválida. Por favor, ingrese un número válido.")

#Ejecución del menú
menu()


