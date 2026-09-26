# Examen práctico - Terminal de Expedición Espacial
# Nombre y apellido: Mirko Julián Sosnovsky Arana
# Curso:2º 1ª
#
# IMPORTANTE:
# Resolver el programa siguiendo las etapas indicadas en el README.md.
# Realizar los commits y push cuando se indique.
#
# No borrar estos comentarios.


# =========================
# ETAPA 1 - INICIO
# =========================

print("TERMINAL DE EXPLORACIÓN ESPACIAL  Nº5")
nopi = input("Ingrese su nombre ")
codi = 100
destinos = ["Luna", "Marte", "Saturno"]
costo = ["20", "35", "50"]
fe = ("fe")
print(f"¡Hola {nopi}, bienvenido!, Para finalizal la expedición ingrese <<fe>> y para consultar el estado de la nave <<CES>>")
print(f"Conbustible disponible = {100} unidades")
ds = ("Sib")
via = int(0)
vialu = int(0)
viama = int(0)
viasa = int(0)
while ds != fe:
    via = vialu+viama+viasa
    print("Destinos posibles: ", destinos)
    print(f"Cantidad de viajes realizados = {via}, Cantidad de viajes realizados a saturno = {viasa}, Cantidad de viajes realizados a marte = {viama}, cantidad de viajes realizados a la luna = {vialu}")
    ds = input("Seleccione un destino escribiéndolo ")
    if ds == "Luna":
        print(f"Destino seleccionado: {ds}")
        print(f"Conbistible necesario: ", costo[0])
        cs = codi-20
        print(f"Conbustible sobrante = {cs}")
        codi = cs
        if cs < 0:
            print("Combustible insuficiente, vuelva a empezar o elija otra ruta")
        else:
            print("Viaje exitoso")
            vialu = vialu+1
    elif ds == "Marte":
        print(f"Destino seleccionado: {ds}")
        print(f"Combustible necesario: ", costo [1])
        cs = codi-35
        print(f"combustible disponible: {cs}")
        codi = cs
        if cs < 0:
            print("Combustible insuficiente, vuelva a empezar o elija otra ruta")
        else:
            print("Viaje exitoso")
            viama = viama+1
    elif ds == "Saturno":
        print(f"Destino elejido: {ds}")
        print(f"Combustible necesario: ", costo [2])
        cs = codi-50
        print(f"Combustible necesaio = {cs}")
        codi = cs
        if cs < 0:
            print("El combustible no alcanza, vuelva a iniciar o intente con otra ruta")
        else:
            print("Viaje exitoso")
            viasa = viasa+1
    elif ds == "CES":
        print(f"Nombre del piloto: {nopi}")
        print(f"Combustible restante: {codi}")
        print(f"Viajes realizados: {via}")
        print(f"Viajes realizados a saturno: {viasa}")
        print(f"Cantidad de viajes realizados a Marte: {viama}")
        print(f"Cantidad de viajes realizados a la Luna: {vialu}")
        for costos in range (1, 2):
            print("saturno - ", costos+49)
            print("Luna - ", costos+19)
            print("Marte - ", costos+34)
    elif ds == fe:
        print("Último resumen: ")
        print(f"Nombre del piloto: {nopi}")
        print(f"Combustible restante: {codi}")
        print(f"Viajes realizados: {via}")
        print(f"Viajes realizados a saturno: {viasa}")
        print(f"Cantidad de viajes realizados a Marte: {viama}")
        print(f"Cantidad de viajes realizados a la Luna: {vialu}")
        for costos in range (1, 2):
            print("saturno - ", costos+49)
            print("Luna - ", costos+19)
            print("Marte - ", costos+34)

        print(f"{nopi}, Gracias por viajar abordo de <<Nave en Sib, 0645>>, ¡Vuelva pronto!")
    else:
        print("No se reconoció el destino, chequeá de que esté bien escrito y que la primer letra sea una mayúscula")

# ¡¡ACORDATE QUE CAMVIASTE "5" POR "fe"!!

# Crear las variables necesarias.
# Crear las listas de destinos y costos.
# Pedir el nombre del piloto.


# =========================
# ETAPA 2 - NAVEGACIÓN
# =========================

# Mostrar el menú y procesar la opción seleccionada.
# Utilizar las listas para obtener destino y costo.


# =========================
# ETAPA 3 - CICLO PRINCIPAL
# =========================

# Modificar el programa para que continúe funcionando
# hasta que el usuario decida finalizar la expedición.


# =========================
# ETAPA 4 - ESTADO Y RESUMEN
# =========================

# Mostrar el estado de la nave.
# Recorrer las listas con un for para mostrar destinos y costos.