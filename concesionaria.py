import random

def rellenar_lista(template):
    nuevo = []
    for marca in template:
        marca_modelo = []
        for modelo in marca:
            ano = random.randint(2000, 2020)
            kms = random.randint(80000, 150000)
            marca_modelo.append([modelo, ano, kms])
            nuevo.append(marca_modelo)
    return nuevo

def crear():
    template = [
        random.sample(toyota, 2),
        random.sample(ford, 2),
        random.sample(chevrolet, 2),
        random.sample(wolkswagen, 2)
        ]
    nuevo = rellenar_lista(template)
    print("\n- Estos fueron los autos vendidos el último mes.")
    print("_" * 150)
    return nuevo


toyota = ["Hilux", "Sw4", "Corolla", "Etios", "Prado"]
ford = ["Focus", "Eco-Sport", "Mondeo", "Ranger", "Fiesta", "Fiesta Kinetic"]
chevrolet = ["S-10", "Cruze", "Prisma", "Tracker"]
wolkswagen = ["Gol", "Amarok", "Bora", "Vento", "Passat", "Surán"]

crear_lista = crear()
print(crear_lista)
