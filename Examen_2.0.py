print("TERMINAL DE EXPLORACIÓN ESPACIAL  Nº5,  Galileo")
nopi = input("Ingrese su nombre ")
codi = 100
res = int(50)
comi = int(1000)
destinos = ["Luna", "Marte", "Saturno", "Tierra"]
costo = ["20", "35", "50", "40"]
fe = ("fe")
print(f"¡Hola {nopi}, bienvenido a Galileo!, para consultar el estado de la nave ingrese <<CES>> y para finalizal la expedición ingrese <<fe>>. Cuando el combustible se agote es nesesario volver a la tierra para cargar más, para eso está la reserva de combustible con 50 unidades, de las cuales se necesita 40 unidades para llegar a la tierra. Para pasar combustible de un tanque a otro ingrese <<Pasar-Combustible>>. Para que este mensaje se repita preciona <<5>>.")
print(f"Conbustible disponible = {100} unidades")
ds = ("Sib")
via = int(0)
vialu = int(0)
viama = int(0)
viasa = int(0)
viati = int(0)
pl = int(0)
are = int(50)
coditot = codi+res
while ds != fe:
    if coditot < 0:
        print("Te quedaste sin combustible, ahora estás varado en el espacio hasta que alguien venga a rescatarte. No te podés comunicar porque no queda nada de combustible.")
        ds = fe
    elif comi < 0:
        print("Te quedaste sin comida, ahora tu destino es morir de hambre en esta nave.")
        ds = fe
    elif are < 0:
        print("Tu nave se rompió, no hay forma de que te rescaten. Tu destino es morir aquí de hambre cuando se te acabe la comida.")
        de = fe
    via = vialu+viama+viasa+viati
    for destino in destinos:
        print("Destino posibles: ", destino)
    print(f"Cantidad de viajes realizados = {via}, Cantidad de viajes realizados a saturno = {viasa}, Cantidad de viajes realizados a marte = {viama}, cantidad de viajes realizados a la luna = {vialu}, cantidad de viajes realizados a la tierra = {viati}")
    ds = input("Seleccione un destino escribiéndolo. Para pasar combustible de un tanque al otro ingrese <<Pasar-Combustible>> ")
    if ds == "Luna":
        print(f"Destino seleccionado: {ds}")
        print(f"Conbistible necesario: ", costo[0])
        cs = codi-20
        print(f"Conbustible sobrante = {cs}")
        codi = cs
        if cs < 0:
            print("Combustible insuficiente, vuelva a empezar o elija otra ruta")
            codi = int(0)
            print("¿Queres volver a la tierra a buscar más combuetible o preferís pasar combustible de la reserva para ir a otro planeta?")
            compa = int(input("Ingrese el número de combustible de la reserva que quiere pasar al tanque principal."))
            if compa > res:
                while compa > res:
                    print(f"No hay {compa} unidades de combustible, ingrese una cifra menor o igual a {res}")
                    compa = int(input("Ingrese la cantidad de combustible que quiere pasar "))
                print("¡Transferencia exitosa!")
                codi = codi+compa
                res = res-compa
            else:
                print("¡Transferencia exitosa!")
                res = res-compa
                codi = codi+compa
                print("Viaje exitoso")
                vialu = vialu+1
                are = are-5
                pl = pl+295
                comi = comi-150
        else:
            print("Viaje exitoso")
            vialu = vialu+1
            are = are-4
            pl = pl+310
            comi = comi-130
    elif ds == "Marte":
        print(f"Destino seleccionado: {ds}")
        print(f"Combustible necesario: ", costo [1])
        cs = codi-35
        print(f"combustible disponible: {cs}")
        codi = cs
        if cs < 0:
            print("Combustible insuficiente, vuelva a empezar o elija otra ruta")
            codi = int(0)
            print("¿Queres volver a la tierra a buscar más combuetible o preferís pasar combustible de la reserva para ir a otro planeta?")
            compa = int(input("Ingrese el número de combustible de la reserva que quiere pasar al tanque principal."))
            if compa > res:
                while compa > res:
                    print(f"No hay {compa} unidades de combustible, ingrese una cifra menor o igual a {res}")
                    compa = int(input("Ingrese la cantidad de combustible que quiere pasar "))
                print("¡Transferencia exitosa!")
                codi = codi+compa
                res = res-compa
            else:
                print("¡Transferencia exitosa!")
                print("Viaje exitoso")
                viama = viama+1
                are = are-7
                pl = pl+445
                comi = comi-200
        else:
            print("Viaje exitoso")
            viama = viama+1
            are = are-6
            pl = pl+475
            comi = comi-175
    elif ds == "Saturno":
        print(f"Destino elejido: {ds}")
        print(f"Combustible necesario: ", costo [2])
        cs = codi-50
        print(f"Combustible necesaio = {cs}")
        codi = cs
        if cs < 0:
            print("Combustible insuficiente, vuelva a empezar o elija otra ruta")
            codi = int(0)
            print("¿Queres volver a la tierra a buscar más combuetible o preferís pasar combustible de la reserva para ir a otro planeta?")
            compa = int(input("Ingrese el número de combustible de la reserva que quiere pasar al tanque principal."))
            if compa > res:
                while compa > res:
                    print(f"No hay {compa} unidades de combustible, ingrese una cifra menor o igual a {res}")
                    compa = int(input("Ingrese la cantidad de combustible que quiere pasar "))
                print("¡Transferencia exitosa!")
                codi = codi+compa
                res = res-compa
            else:
                print("¡Transferencia exitosa!")
                print("Viaje exitoso")
                viasa = viasa+1
                are = are-11
                pl = pl+495
                comi = comi-250
        else:
            print("Viaje exitoso")
            viasa = viasa+1
            are = are-10
            pl = pl+625
            comi = comi-220
    elif ds == "Tierra":
        print(f"Destino elejido: {ds}")
        print(f"Combustible necesario: ", costo [3])
        cs = codi-40
        print(f"Combustible total = {cs}")
        codi = cs
        if cs < 0:
            print("Combustible insuficiente, vuelva a empezar o elija otra ruta")
            codi = int(0)
            print("¿Queres volver a la tierra a buscar más combuetible o preferís pasar combustible de la reserva para ir a otro planeta?")
            compa = int(input("Ingrese el número de combustible de la reserva que quiere pasar al tanque principal."))
            if compa > res:
                while compa > res:
                    print(f"No hay {compa} unidades de combustible, ingrese una cifra menor o igual a {res}")
                    compa = int(input("Ingrese la cantidad de combustible que quiere pasar "))
                print("¡Transferencia exitosa!")
                codi = codi+compa
                res = res-compa
                comi = comi-215
            else:
                print("¡Transferencia exitosa!")
                res = res-compa
                codi = codi+compa
                pl = pl+175
                are = are-10
                comi = comi-200
        else:
            print("Viaje exitoso")
            viati = viasa+1
            pl = pl+100
            are = are-8
            print("ESTADO DE LA NAVE")
            print(f"Nombre del piloto: {nopi}")
            print(f"Comida: {comi}")
            print(f"Combustible restante: {codi}")
            print(f"Combustible de reserva: {res}")
            print(f"Cantidad de viajes realizados: {via}")
            print(f"Cantidad de viajes realizados a saturno: {viasa}")
            print(f"Cantidad de viajes realizados a Marte: {viama}")
            print(f"Cantidad de viajes realizados a la Luna: {vialu}")
            print(f"Cantidad de viajes realizados a la tierra: {viati}")
            print(f"Plata: {pl}")
            print(f"Estado de la nave (reparación): {are}")
            for costos in range (1, 2):
                print("saturno - ", costos+49)
                print("Luna - ", costos+19)
                print("Marte - ", costos+34)
                inv = "Sib"
            while inv != "Nada-Más":
                inv = input("¿En qué queres invertir? (Combustible, Comida, Arreglos-de-la-nave, Mejoras-de-la-nave) Ingresa la inverción escribiéndola talcual aparece ahí. Cuando termines ingresá <<Nada-Más>>")
                if inv == "Combustible":
                    codin = int(input("Ingrese la cantidad de plata que quiere invertir en combustible, cada unidad vale 10 pesos "))
                    while codin > pl:
                        print(f"No hay {codin} pesos para invertir, tenés {pl}")
                        codin = int(input("Ingrese la cantidad de plata que quiere invertir en combustible, cada unidad vale 10 pesos "))

                    pl = pl-codin
                    codit = codin/10
                    codi = codi+codit
                    print(f"Inverción exitosa, invertiste {codin} pesos en combustible, ahora tenés {codi} unidades y te quedan {pl} pesos.")
                elif inv == "Arreglos-de-la-nave":
                    mej = int(input(f"Tenés {are} puntos de arreglo, cada uno sale 2 pesos, ¿Cuánta plata querés invertir?"))
                    while mej > pl:
                        print(f"No hay {mej} pesos para invertir, tenés {pl} pesos.")
                        mej == int(input(f"Tenés {are} puntos de arreglo, cada uno sale 2 pesos, ¿Cuánta plata querés invertir?"))

                    pl = pl-mej
                    mejo = mej/2
                    are = are+mejo
                elif inv == "Comida":
                    com = int(input(f"Tenés {comi} puntos de comida, cada puntosale 5 pesos, ¿Cuánta plata queres invertir?"))
                    while com > pl:
                        print(f"No hay {com} pesos para invertir, tenés {pl} pesos.")
                        com = int(input("Tenés {comi} puntos de comida, cada puntosale 5 pesos, ¿Cuánta plata queres invertir?"))

                    pl = pl-com
                    comid = com/5
                    comi = comi+comid
                elif inv == "Nada-Más":
                    print("¡Ya estás listo para salir nuevamente!")
                elif ds == "CES":
                    print(f"Nombre del piloto: {nopi}")
                    print(f"Comida restante: {comi}")
                    print(f"Combustible restante: {codi}")
                    print(f"Combustible de reserva: {res}")
                    print(f"Cantidad de viajes realizados: {via}")
                    print(f"Cantidad de viajes realizados a saturno: {viasa}")
                    print(f"Cantidad de viajes realizados a Marte: {viama}")
                    print(f"Cantidad de viajes realizados a la Luna: {vialu}")
                    print(f"Cantidad de viajes realizados a la tierra: {viati}")
                    print(f"Plata: {pl}")
                    print(f"Estado de la nave (reparación): {are}")
                    for costos in range (1, 2):
                        print("saturno - ", costos+49)
                        print("Luna - ", costos+19)
                        print("Marte - ", costos+34)
                else:
                    print(f"Nose encontró {inv}, por favor chequeá de haberlo escrito correctamente")


    elif ds == "Pasar-Combustible":
        tan = input("¿De qué tanque a que tanque quiere pasar el combustible? Si es de la reserva al principal escriba <<RaP>>, si es del principal a la reserva escriba <<PaR>> (Sin las comillas <<>>)")
        if tan == "PaR":
            compa = int(input("Ingrese la cantidad de combustible que quiere pasar "))
            while compa > codi:
                print(f"No hay {compa} unidades de combustible, ingrese una cifra menor o igual a {codi}")
                compa = int(input("Ingrese la cantidad de combustible que quiere pasar "))

            print("¡Transferencia exitosa!")
            res = res+compa
            codi = codi-compa
        elif tan == "RaP":
            compa = int(input("Ingrese la cantidad de combustible que quiere transferir "))
            while compa > res:
                print(f"No hay {compa} unidades de combustible, ingrese una cifra menor o igual a {res}")
                compa = int(input("Ingrese la cantidad de combustible que quiere pasar "))

            print("¡Transferencia exitosa!")
            codi = codi+compa
            res = res-compa
    elif ds == "5":
        print(f"¡Hola {nopi}, para consultar el estado de la nave ingrese <<CES>> y para finalizal la expedición ingrese <<fe>>. Cuando el combustible se agote es nesesario volver a la tierra para cargar más, para eso está la reserva de combustible con 50 unidades, de las cuales se necesita 40 unidades para llegar a la tierra. Para pasar combustible de un tanque a otro ingrese <<Pasar-Combustible>>. Para que este mensaje se repita preciona <<5>>.")
    elif ds == "CES":
                print(f"Nombre del piloto: {nopi}")
                print(f"Comida restante: {comi}")
                print(f"Combustible restante: {codi}")
                print(f"Combustible de reserva: {res}")
                print(f"Cantidad de viajes realizados: {via}")
                print(f"Cantidad de viajes realizados a saturno: {viasa}")
                print(f"Cantidad de viajes realizados a Marte: {viama}")
                print(f"Cantidad de viajes realizados a la Luna: {vialu}")
                print(f"Cantidad de viajes realizados a la tierra: {viati}")
                print(f"Plata: {pl}")
                print(f"Estado de la nave (reparación): {are}")
                for costos in range (1, 2):
                    print("saturno - ", costos+49)
                    print("Luna - ", costos+19)
                    print("Marte - ", costos+34)
    elif ds == fe:
        print("Último resumen: ")
        print(f"Nombre del piloto: {nopi}")
        print(f"Combustible restante: {codi}")
        print(f"Combustible de reserva: {res}")
        print(f"Comida restante: {comi}")
        print(f"Cantidad de viajes realizados: {via}")
        print(f"Cantidad de viajes realizados a saturno: {viasa}")
        print(f"Cantidad de viajes realizados a Marte: {viama}")
        print(f"Cantidad de viajes realizados a la Luna: {vialu}")
        print(f"Viajes a la tierra: {viati}")
        print(f"Plata: {pl}")
        print(f"Estado de la nave (reparación): {are}")
        for costos in range (1, 2):
            print("saturno - ", costos+49)
            print("Luna - ", costos+19)
            print("Marte - ", costos+34)

        print(f"{nopi}, Gracias por viajar abordo de <<Nave en Sib, 0645>>, ¡Vuelva pronto!")
    else:
        print("No se reconoció el destino, chequeá de que esté bien escrito y que la primer letra sea una mayúscula")

