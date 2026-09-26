print("TERMINAL DE EXPLORACIÓN ESPACIAL  Nº5,  Galileo")
nopi = input("Ingrese su nombre ")
codi = 100
res = int(50)
comi = int(1000)
destinos = ["Luna", "Marte", "Saturno", "Tierra", "Venus"]
costo = ["20", "35", "50", "40", "30"]
fe = ("fe")
print(f"¡Hola {nopi}, bienvenido a Galileo!, para consultar el estado de la nave ingrese <<CES>> y para finalizal la expedición ingrese <<fe>>. Cuando el combustible se agote es nesesario volver a la tierra para cargar más, para eso está la reserva de combustible con 50 unidades, de las cuales se necesitan 40 unidades para llegar a la tierra. Para pasar combustible de un tanque a otro ingrese <<Pasar-Combustible>>. Para que este mensaje se repita preciona <<5>>.")
print(f"Conbustible disponible = {100} unidades")
ds = ("Sib")
viave = int(0)
vialu = int(0)
viama = int(0)
viasa = int(0)
viati = int(0)
via = int(0)
pl = int(0)
are = int(50)
coditot = codi+res
while ds != "fe":
    if coditot < 20:
        print("Te quedaste sin combustible, ahora estás varado en el espacio hasta que alguien venga a rescatarte. No te podés comunicar porque no queda nada de combustible.")
        ds = fe
    elif comi <90:
        print("Te queda poca comida, Tenés que ir a la tierra a buscar más")
    elif comi < 0:
        print("Te quedaste sin comida, ahora tu destino es morir de hambre en esta nave.")
        comi = int(-1)
        ds = "fe"
    elif are < 10:
        print("Tu nave está a punto de romperse, tenés que ir a la tierra a arreglarla")
    elif are < 0:
        print("Tu nave se rompió, no hay forma de que te rescaten. Tu destino es morir aquí de hambre cuando se te acabe la comida.")
        de = fe
    via = vialu+viama+viasa+viati+viave
    for costos in range (1, 2):
        print("saturno - ", costos+49)
        print("Luna - ", costos+19)
        print("Marte - ", costos+34)
        print(f"Venus - ", costos+29)
    print(f"Cantidad de viajes realizados = {via}")
    print(f"Cantidad de viajes realizados a saturno = {viasa}")
    print(f"Cantidad de viajes realizados a marte = {viama}")
    print(f"Cantidad de viajes realizados a la luna = {vialu}")
    print(f"cantidad de viajes realizados a la tierra = {viati}")
    ds = input("Seleccione un destino escribiéndolo. Para pasar combustible de un tanque al otro ingrese <<Pasar-Combustible>> ")
    if ds == "Luna":
        print(f"Destino seleccionado: {ds}")
        print(f"Conbistible necesario: ", costo[0])
        cs = codi-20
        print(f"Conbustible sobrante = {cs}")
        codi = cs
        if coditot < 20:
            print("Te quedaste sin combustible, ahora estás varado en el espacio hasta que alguien venga a rescatarte. No te podés comunicar porque no queda nada de combustible.")
            ds = fe
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
                pl = pl+410
                comi = comi-70
        else:
            print("Viaje exitoso")
            vialu = vialu+1
            are = are-4
            pl = pl+520
            comi = comi-50
    elif ds == "Venus":
        print(f"Destino seleccionado: {ds}")
        print(f"Combustible necesario: ", costo [4])
        cs = codi-30
        print(f"Combustible sobrente: {ds}")
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
                are = are-12
                pl = pl+780
                comi = comi-80
                print("¡Bienvenido a Venus!, el segundo planeta del sistema solar, también conocido como el planeta rojo. Venus se encuentra a aproximada mente 108 millones de kilómetros del sol, y en su punto más cercano a 40 millones de kilómetros de la tierra.")
                if viave == 1:
                    print("Venu está cubierto por una espesa y cerrada capa de nubes compuestas de gotas de ácido letales, que reflejan al sol. Con un grosor de 25 KM, las nubes impiden que gran parte de la luz del sol no alcanza la superficie, pero sí que llega otro tipo de radiación llamada infrarroja, que queda atrapada por la densa atmósfera.")
                elif viave == 2:
                    print("Venus está cubierto por una atmósfera densa de  dióx dióxido de carbono, y sus nubes son de ácido sulfúico. Ambos forman el llamado efecto invernadero: atrapan el calor y calientan el planeta. Venus puede alcanzar temperatura insoportables, la máxima es de  453 ℃ y la mínima es de menos 45 °C.")
                elif viave == 3:
                    print("Se han registrado unos 1600 grandes volcanes en Venus, a los que se suman centenares de miles de volcanes menores. Hace años que los astrónomos vienen debatiendo si alguno de estos volcanes puede estar activo en la actualidad")
                elif viave == 4:
                    print("  El hierro que hay en sus rocas y el polvo se vuelven óxido de hierro. Es por esto que el planeta se ve rojo a simple vista cuando lo vemos en el cielo.")
                elif viave == 5:
                    print("Tamaño: Es muy similar a la Tierra, con un diámetro de 12.104 kilómetros (la Tierra tiene 12.756 km). Rotación: Gira en dirección contraria a la mayoría de los planetas y lo hace muy lento. Un día en Venus (243 días terrestres) dura más que su año (225 días terrestres)")
                else:
                    print(" ")
        else:
            print("Viaje exitoso")
            viama = viama+1
            are = are-10
            pl = pl+900
            comi = comi-60
            print("¡Bienvenido a Venus!, el segundo planeta del sistema solar, también conocido como el planeta rojo. Venus se encuentra a aproximada mente 108 millones de kilómetros del sol, y en su punto más cercano a 40 millones de kilómetros de la tierra.")
            if viave == 1:
                print("Venu está cubierto por una espesa y cerrada capa de nubes compuestas de gotas de ácido letales, que reflejan al sol. Con un grosor de 25 KM, las nubes impiden que gran parte de la luz del sol no alcanza la superficie, pero sí que llega otro tipo de radiación llamada infrarroja, que queda atrapada por la densa atmósfera.")
            elif viave == 2:
                print("Venus está cubierto por una atmósfera densa de  dióx dióxido de carbono, y sus nubes son de ácido sulfúico. Ambos forman el llamado efecto invernadero: atrapan el calor y calientan el planeta. Venus puede alcanzar temperatura insoportables, la máxima es de  453 ℃ y la mínima es de menos 45 °C.")
            elif viave == 3:
                print("Se han registrado unos 1600 grandes volcanes en Venus, a los que se suman centenares de miles de volcanes menores. Hace años que los astrónomos vienen debatiendo si alguno de estos volcanes puede estar activo en la actualidad")
            elif viave == 4:
                print("  El hierro que hay en sus rocas y el polvo se vuelven óxido de hierro. Es por esto que el planeta se ve rojo a simple vista cuando lo vemos en el cielo.")
            elif viave == 5:
                print("Tamaño: Es muy similar a la Tierra, con un diámetro de 12.104 kilómetros (la Tierra tiene 12.756 km). Rotación: Gira en dirección contraria a la mayoría de los planetas y lo hace muy lento. Un día en Venus (243 días terrestres) dura más que su año (225 días terrestres)")
            else:
                    print(" ")
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
                pl = pl+745
                comi = comi-80
        else:
            print("Viaje exitoso")
            viama = viama+1
            are = are-6
            pl = pl+850
            comi = comi-60
    elif ds == "Saturno":
        print(f"Destino elejido: {ds}")
        print(f"Combustible necesario: ", costo [2])
        cs = codi-50
        print(f"Combustible sobrante = {cs}")
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
                pl = pl+800
                comi = comi-90
        else:
            print("Viaje exitoso")
            viasa = viasa+1
            are = are-10
            pl = pl+970
            comi = comi-80
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
            else:
                print("¡Transferencia exitosa!")
                res = res-compa
                codi = codi+compa
                pl = pl+75
                are = are-10
                comi = comi-90
                viati = viati+1
        else:
            print("Viaje exitoso")
            viati = viati+1
            via = via+1
            comi = comi-70
            pl = pl+100
            are = are-8
            print("")
            print("     ESTADO DE LA NAVE")
            print("")
            print(f"Nombre del piloto: {nopi}")
            print(f"Comida: {comi}")
            print(f"Combustible restante: {codi}")
            print(f"Combustible de reserva: {res}")
            print(f"Cantidad de viajes realizados: {via}")
            print(f"Cantidad de viajes realizados a saturno: {viasa}")
            print(f"Cantidad de viajes realizados a Marte: {viama}")
            print(f"Cantidad de viajes realizados a la Luna: {vialu}")
            print(f"Cantidad de viajes realizados a la tierra: {viati}")
            print(f"Cantidad de viajes realizados a venus: {viave}")
            print(f"Plata: {pl}")
            print(f"Estado de la nave (reparación): {are}")
            for costos in range (1, 2):
                print("saturno - ", costos+49)
                print("Luna - ", costos+19)
                print("Marte - ", costos+34)
                inv = "Sib"
            while inv != "Nada-Más":
                inv = input("¿En qué querés invertir? (Combustible, Comida, Arreglos-de-la-nave, Mejoras-de-la-nave) Ingresa la inverción escribiéndola talcual aparece ahí. Cuando termines ingresá <<Nada-Más>>")
                if inv == "Combustible":
                    codin = int(input("Ingrese la cantidad de plata que quiere invertir en combustible, cada unidad vale 10 pesos "))
                    while codin > pl:
                        print(f"No hay {codin} pesos para invertir, tenés {pl}")
                        codin = int(input("Ingrese la cantidad de plata que quiere invertir en combustible, cada unidad vale 10 pesos "))

                    pl = pl-codin
                    codit = codin/10
                    codi = codi+codit
                    print(f"¡Inversión exitosa!, invertiste {codin} pesos en combustible, ahora tenés {codi} unidades y te quedan {pl} pesos.")
                elif inv == "Arreglos-de-la-nave":
                    mej = int(input(f"Tenés {are} puntos de arreglo, cada uno sale 2 pesos, ¿Cuánta plata querés invertir? "))
                    while mej > pl:
                        print(f"No hay {mej} pesos para invertir, tenés {pl} pesos.")
                        mej = int(input(f"Tenés {are} puntos de arreglo, cada uno sale 2 pesos, ¿Cuánta plata querés invertir? "))

                    pl = pl-mej
                    mejo = mej/2
                    are = are+mejo
                    print(f"¡Inversión exitosa!, invertiste {mej} pesos en arreglos y ahora tenés {are} puntos de arreglos y te quedan {pl} pesos.")
                elif inv == "Comida":
                    com = int(input(f"Tenés {comi} puntos de comida, cada puntosale 5 pesos, ¿Cuánta plata queres invertir? "))
                    while com > pl:
                        print(f"No hay {com} pesos para invertir, tenés {pl} pesos.")
                        com = int(input("Tenés {comi} puntos de comida, cada puntosale 5 pesos, ¿Cuánta plata queres invertir? "))

                    pl = pl-com
                    comid = com/5
                    comi = comi+comid
                    print(f"¡Inversión exitosa!, invertiste {com} pesos en comida y ahora te quedan {pl} pesos.")
                elif inv == "Nada-Más":
                    print("¡Ya estás listo para salir nuevamente!")
                elif inv == "CES":
                    print(f"Nombre del piloto: {nopi}")
                    print(f"Comida restante: {comi}")
                    print(f"Combustible restante: {codi}")
                    print(f"Combustible de reserva: {res}")
                    print(f"Cantidad de viajes realizados: {via}")
                    print(f"Cantidad de viajes realizados a saturno: {viasa}")
                    print(f"Cantidad de viajes realizados a Marte: {viama}")
                    print(f"Cantidad de viajes realizados a la Luna: {vialu}")
                    print(f"Cantidad de viajes realizados a la tierra: {viati}")
                    print(f"Cantidad de viajes realizados a venus: {viave}")
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
                print(f"Cantidad de viajes realizados a venus {viave}")
                print(f"Plata: {pl}")
                print(f"Estado de la nave (reparación): {are}")
                for costos in range (1, 2):
                    print("saturno - ", costos+49)
                    print("Luna - ", costos+19)
                    print("Marte - ", costos+34)
    elif ds == "Aguante la Música Clásica":
        print(f"Trnés toda la razón, ¡{ds}!")
        pl = pl*2
        are = are*2
        comi = comi*3
        codi = codi*2
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
        print(f"Cantidad de viajes a la tierra: {viati}")
        print(f"Cantidad de viajes realizados a venus {viave}")
        print(f"Plata: {pl}")
        print(f"Estado de la nave (reparación): {are}")
        for costos in range (1, 2):
            print("saturno - ", costos+49)
            print("Luna - ", costos+19)
            print("Marte - ", costos+34)

        print(f"{nopi}, Gracias por viajar abordo de <<Nave en Sib, 0645>>, ¡Vuelva pronto!")
    else:
        print("No se reconoció el destino, chequeá de que esté bien escrito y que la primer letra sea una mayúscula")