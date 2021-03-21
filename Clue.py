# Christian Márquez Garza   18310180    6E1

import random

person = ["Dracon", "Lia", "Melvina", "Rodan", "Han"]
place = ["Jardin", "Entrada principal", "Escaleras", "Departamento de la victima", "Azotea"]
Weapon = ["Cadena","Bate","Cuchillo","Pedazo de vidrio","Machete"]
Killer = ["None", "None", "None"]
Register = ["None", "None", "None"]
Fatal = ["tirado, parece haberse del tercer piso", "colgado en uno de los barandales", "en la entrada de su departamento con varias heridas."]
Nei = ["Tomas","Minho","Newt","Albi"]
random.shuffle(Fatal)
random.shuffle(Nei)
Intro = []                                          # Valores elegidos
mood = ["None", "None", "None", "None", "None"]     # Conversacion de los hechos
Des = ["None", "None", "None", "None", "None"]      # Descripcion de los escenarios
Look = []                                           # Lo que se apredica en el departamento
Get1 = ["",""]
Get2 = []
per = [0,1,2,3,4]
lug = [0,1,2,3,4]
special = 0
pase = ""
Menu = ["1. Indagar a uno de los sospechosos", "2. Revisar alguna área", "3. Dar el veredicto", "4. No hacer nada"]
Men = [1 ,2 ,3 ,4]

def Game():
    random.shuffle(person)
    random.shuffle(Weapon)
    random.shuffle(place)
    Killer[0] = random.choice(person)
    Killer[1] = random.choice(place)
    Killer[2] = random.choice(Weapon)

    #  Perfiles
    P = ["trabaja en una modelorama, ", "administra una tienda naturista, ", "su local es una panaderia, ",
         "tiene su propia farmacia, ", "su local es <La hormiga> es una ferreteria completa, "]
    A = ["suele estar alegre. ", "es una persona seria. ", "me cae bien como persona. ", "tiene una expresion molesta. ",
         "a veces se ve triste. "]
    Buzz = ["Atiende la puerta", "Tardo un poco en abrir", "Estaba a punto de salir",
            "No responde, quizas no se encuntra en casa",
            "Abre de inmediato"]

    random.shuffle(P)
    random.shuffle(A)
    random.shuffle(Buzz)

    for i in range(5):
        if Buzz[i] == "No responde, quizas no se encuntra en casa":
            special = i
            pase = person[i]
        Intro.append(P[i] + A[i] + Buzz[i])

    I1 = ["¿Que haces aqui?", "¿En que puedo ayudarte?", "¿Que te trae por aqui?", "¿Ya viste la hora que es?",
          "Buenas tardes", "Un gusto verte", "¿Necesitas algo?", "Que tal", "¿Como va todo?"]
    I2 = ["¿Que tienen de buenos?", "¿Que quieres?", "Dime lo que necesitas", "¿Que se te ofrece?", "Buenas",
          "¿Puedo ayudarte en algo?", "¿A que se debe la interrupcion?"]

    random.shuffle(I1)
    random.shuffle(I2)

    for i in range(0,2):
        Get2.append(I2[i])

    for i in range(2,5):
        Get1.append(I1[i])

    x = 0
    y = 0
    i = 0

    wea = Killer[2]
    if wea == "Cadena":
        wea = "una {}".format(wea)
    else:
        wea = "un {}".format(wea)
    Con1 = ["una Cadena", "un Bate", "un Cuchillo", "un Pedazo de vidrio", "un Machete"]
    Con1.remove(wea)

    if wea == "una Cadena":
        wea = "{} manchada".format(wea)
    else:
        wea = "{} manchado".format(wea)
    Con1.append(wea)
    random.shuffle(Con1)

    count1 = 0

    arma = random.choice(Con1)

    Jar = ["recuerdo haber estado aqui en la mañana, y se ve en diferente estado, se puede observar pisoteado",
           "miras determinadamente, la basura se ve movida y encuentras {}".format(arma),
           "parece que lo acaban de arreglar hace poco, las bancas se ven un poco sucias",
           "miro determinadamente, tiene las paredes sucias y mucha basura regada, necesita un arreglo"]

    if Killer[1] == "Jardin":
        comienza = random.randint(0, 1)
        if comienza == 0:
            Des[place.index("Jardin")] = Jar[1]
            Con1.remove(arma)
            count1 += 1
        else:
            Des[place.index("Jardin")] = Jar[0]
    else:
        i = random.randint(1,3)
        Des[place.index("Jardin")] = Jar[i]
        if i == 1:
            Con1.remove(arma)
            count1 += 1

    arma = random.choice(Con1)

    EP = ["al mirar con detalle te percatas que las persianas parecen abolladas, no recuerdas si asi estaban antes",
          "nadie esta entrando y saliendo, reviso los costados y frente a un local encuentro {}".format(arma),
          "la empresa contrato a alguien para darle mantenimiento e instalar camaras de seguridad, para evitar otra desgracia",
          "nadie esta fuera y se ve solo, los locales estan cerrado y la basura se la acaban de llevar"]

    if Killer[1] == "Entrada principal":
        comienza = random.randint(0, 1)
        if comienza == 0:
            Des[place.index("Entrada principal")] = EP[1]
            Con1.remove(arma)
            count1 += 1
        else:
            Des[place.index("Entrada principal")] = EP[0]
    else:
        i = random.randint(1, 3)
        Des[place.index("Entrada principal")] = EP[i]
        if i == 1:
            Con1.remove(arma)
            count1 += 1

    arma = random.choice(Con1)

    Esc = ["mientras subes y bajas detectas que el barandal rechina mucho, cosa que no sucedia hace unos dias",
           "no hay mucho que analizar, debajo de las escaleras en el piso, se puede observar un {} ".format(arma),
           "reviso las escaleras de todos los pisos, le hace falta una limpiada al barandal",
           "recuerdo que hace dos dias lo limpiaron bien, si algo paso aqui, quedo bien encubierto",]

    if Killer[1] == "Escaleras":
        if count1 == 0:
            Des[place.index("Azotea")] = Esc[random.randint(1, 2)]
            Con1.remove(arma)
            count1 += 1
        else:
            comienza = random.randint(0, 1)
            if comienza == 0:
                Des[place.index("Escaleras")] = Esc[1]
                Con1.remove(arma)
                count1 += 1
            else:
                Des[place.index("Escaleras")] = Esc[0]
    else:
        if count1 == 0:
            Des[place.index("Escaleras")] = Esc[1]
            Con1.remove(arma)
            count1 += 1
        else:
            i = random.randint(1, 3)
            Des[place.index("Escaleras")] = Esc[i]
            if i == 1:
                Con1.remove(arma)
                count1 += 1

    arma = random.choice(Con1)

    DdlV = ["entré y tiene muchas cosas tiradas, parece que el no desordeno su cuarto",
            "la puerta quedo abierta, el lugar parece un chiquero, sus sabanas estan aventadas, en la sala se observa {}".format(arma),
            "parece que tiene llave, echo un vistazo por la ventana y lo que puedo observar es {}".format(arma),
            "parece que tiene llave, echo un vistazo por la ventana y lo que puedo observar es las sobras de la cena",
            "no recuerdo el departamento abierto, se ve organizado, tanto que siento que han robado aqui"]

    if Killer[1] == "Departamento de la victima":
        if count1 ==1:
            Des[place.index("Azotea")] = DdlV[random.randint(1, 2)]
            Con1.remove(arma)
            count1 += 1
        else:
            comienza = random.randint(0, 1)
            if comienza == 0 and count1 != 3:
                Des[place.index("Departamento de la victima")] = DdlV[random.randint(1,2)]
                Con1.remove(arma)
                count1 += 1
            else:
                Des[place.index("Departamento de la victima")] = DdlV[0]
    else:
        if count1 == 3:
            i = random.randint(3, 4)
            Des[place.index("Departamento de la victima")] = DdlV[i]
        elif count1 == 1:
            Des[place.index("Departamento de la victima")] = DdlV[random.randint(1, 2)]
            Con1.remove(arma)
            count1 += 1
        else:
            i = random.randint(1, 4)
            Des[place.index("Departamento de la victima")] = DdlV[i]
            if i == 1 or i == 2:
                Con1.remove(arma)
                count1 += 1

    arma = random.choice(Con1)

    Az = ["encuentro un par de plantas arrancadas y tierra tirada, empiezo a mover para saber si encuentro algo pero no hay nada",
          "se ve verde, buscas entre los arbustos y encuentras un {}, quizas lleva dias, esta muy al fondo".format(arma),
          "buscas entre los arbustos, y revisas la tierra, lo unico que puedes observar es {}".format(arma) ,
          "la brisa se siente agradable, con ganas de acostarte en la silla de playa, varios muebles se ve fuera de su lugar",
          "encuentras un libro de interes social, lo guardas para ver quien lo reclama, faltan botes de basura aqui arriba"]

    if Killer[1] == "Azotea":
        if count1 ==2:
            Des[place.index("Azotea")] = Az[random.randint(1, 2)]
            Con1.remove(arma)
            count1 += 1
        else:
            comienza = random.randint(0, 1)
            if comienza == 0 and count1 != 3:
                Des[place.index("Azotea")] = Az[random.randint(1, 2)]
                Con1.remove(arma)
                count1 += 1
            else:
                Des[place.index("Azotea")] = Az[0]
    else:
        if count1 == 3:
            i = random.randint(3, 4)
            Des[place.index("Azotea")] = Az[i]
        elif count1 == 2:
            Des[place.index("Azotea")] = Az[random.randint(1, 2)]
            count1 += 1
            Con1.remove(arma)
        else:
            i = random.randint(3, 4)
            Des[place.index("Azotea")] = Az[i]

#***********************************************************************************************************************

    ele = []
    count3 = 0
    entro = 0
    n = ""
    m = ""
    nom = ""
    nom1 = ""
    nom2 = ""
    par = -1
    b = 0

    for w in range(5):
        i = 0
        if par >= 0 and Killer[0] != person[w] and m == person[w]:
            if w != special:
                count3 += 1
            i = par
            par = -2
            nom1 = n
            ele.append(i)
        elif (w != special) and (person[w] != Killer[0]):
            comienza = random.randint(0, 1)
            if (comienza == 0 or count3 == 2) and (entro == 0):
                entro = 1
                i = random.randint(9, 11)
                while i in ele:
                    i = random.randint(9, 11)
                nom = Killer[0]
                b = random.randint(0, 4)
                while person.index(Killer[0]) == w and b == w:
                    b = random.randint(0, 4)
                nom2 = person[b]
                ele.append(i)
            else:
                count3 += 1
                if par == -1 and w <= 3:
                    i = random.randint(0, 5)
                    while i in ele:
                        i = random.randint(0, 5)
                    if i == 0 or i == 2 or i == 4:
                        par = i + 1
                    elif i == 1 or i == 3 or i == 5:
                        par = i - 1
                    b = random.randint(w+1, 4)
                    while person.index(Killer[0]) == b or w == b:
                        b = random.randint(w+1, 4)
                    nom1 = person[b]
                    m = person[b]
                    n = person[w]
                    ele.append(i)
                else:
                    i = random.randint(6, 8)
                    while i in ele:
                        i = random.randint(6, 8)
                    ele.append(i)

        elif Killer[0] == person[w]:
            i = random.randint(0, 11)
            while i in ele:
                i = random.randint(0, 11)
            ele.append(i)
            if i == 0 or i == 2 or i == 4:
                ele.append(i + 1)
            elif i == 1 or i == 3 or i == 5:
                ele.append(i - 1)
            a = random.randint(0, 4)
            while person.index(Killer[0]) == a:
                a = random.randint(0,4)
            nom = person[a]
            nom1 = nom
            b = random.randint(0, 4)
            while person.index(Killer[0]) == a or b == a:
                b = random.randint(0,4)
            nom2 = person[b]

        Chats = ["Abri tarde y cerré temprano para ver una película con {} y pase la noche ahi, regresé a mi departamento por la madrugada".format(nom1),
                 "El día estuvo fabuloso, hice muchas ventas, invité a {} a ver una película, dormió conmigo y cuando me levanté no estaba por ningun lado".format(nom1),
                 "Como siempre, el día fue agradable, por la noche compartí una cena con {} y después hablamos hasta quedarnos dormidos".format(nom1),
                 "No fue un buen día, abri y no vinieron clientes, {} y yo nos pusimos de acuerdo para cenar y tuve una charla tranquila".format(nom1),
                 "Atendia mi negocio como todos los dias, {} cerró temprano y se fue a su departamento y no escuché nada durante la noche".format(nom1),
                 "El día de ayer no hubo muchos clientes, no cerré tan tarde y vi la tele antes de dormir",
                 "Ese día fue mi cumpleaños, no acepto felicitaciones atrasadas, trabajé hasta tarde y terminé cansado en mi cama",
                 "Fue un día como cualquier otro, hubo clientes, fue productivo y fui el último local en cerrar, escuché un gato por la madrugada",
                 "Abri temprano el local porque queria irme temprano, tenia una cita por la tarde y no regresé hasta hoy medio día",
                 "Ayer tenia resaca, abri medio día y en el resto me la pase tumbado en el suelo, durante la madrugada vi a {} antes de regresar a mi depa".format(nom),
                 "No fue mi día, me fui a descansar temprano y no recuerdo si subieron {} y {}".format(nom, nom2),
                 "Me sentia mal, trabajé medio día y me levanté a tomar mi medicina a las 4am, recuerdo escuchar a {}".format(nom)]

        mood[w] = Chats[i]

#***********************************************************************************************************************
    notav = []
    notas = []
    count2 = 0
    for w in range(0,5):
        if len(Con1) != 0:
            arma = Con1[random.randint(0, len(Con1)-1)]
        else:
            arma = "None"


        Visual = ["No abre toda la puerta, como si estuvira ocultando algo o tiene algo que no quiere que vean",
                  "El depa parece desordenado, tiene una pila de ropa sucia del día de ayer cercas de la entrada",
                  "Parece haber sido recogido hace poco y tiene productos de limpieza sobre la mesa",
                  "Tiene las llaves en la mano, parece que iba a salir en cuanto lo interrumpiste",
                  "Su cuarto siempre suele estar limpio, llega un olor agradable, entonces limpio hace poco"]

        Suspect = ["El depa parece desordenado, ves ropa sucia que parece haber usado ayer y se puede observar {} en la mesa de noche".format(arma),
                  "Esta la tele prendida y el programa se ve bueno, puedes observar {} cercas de la cocina".format(arma),
                  "Todo el depa parece ordenado, parece que estaba cocinando, ves en el sillon {}".format(arma),]

        if len(notav) >= 1:
            for z in notav[:]:
                Visual.remove(z)

        if Killer[0] == person[w]:
            if (count2 == 0 and w == 3) or (count2 == 1 and w == 4):
                if len(notas) == 1:
                    Suspect.pop(notas[0])
                i = random.randint(0, len(Suspect) - 1)
                Look.append(Suspect[i])
                notas.append(i)
                count2 += 1
                Con1.remove(arma)
            else:
                comienza = random.randint(0, 1)
                if count2 != 2 and comienza == 1:
                    if len(notas) == 1:
                        Suspect.pop(notas[0])
                    i = random.randint(0, len(Suspect) - 1)
                    Look.append(Suspect[i])
                    notas.append(i)
                    count2 += 1
                    Con1.remove(arma)
                else:
                    i = random.randint(0, len(Visual) - 1)
                    Look.append(Visual[i])
                    notav.append(Visual[i])
        else:
            if count2 == 2:
                i = random.randint(0, len(Visual)-1)
                Look.append(Visual[i])
                notav.append(Visual[i])
            elif (count2 == 0 and w == 3) or (count2 == 1 and w == 4):
                if len(notas) == 1:
                    Suspect.pop(notas[0])
                i = random.randint(0, len(Suspect)-1)
                Look.append(Suspect[i])
                notas.append(i)
                Con1.remove(arma)
                count2 += 1
            else:
                comienza = random.randint(0, 1)
                if comienza == 1 and count2 != 2:
                    if len(notas) == 1:
                        Suspect.pop(notas[0])
                    i = random.randint(0, len(Suspect) - 1)
                    Look.append(Suspect[i])
                    notas.append(i)
                    count2 += 1
                    Con1.remove(arma)
                else:
                    i = random.randint(0, len(Visual) - 1)
                    Look.append(Visual[i])
                    notav.append(Visual[i])

    return pase


print("Juego: Crazy killer")

#Bucle para el programa
while True:
    print("Menú")
    print("1. Iniciar el juego \n2. Cerrar el programa\n")
    print("Selección la acción: ")
    while True:
        enter = -1
        enter = input()[0:1]
        #Revisar la entrada
        if (enter in ['1','2']) == False:
            print("No existe la opción")
        else:
            break

    if enter == '1':
        print("La empresa Supernova tiene una plaza ubicada en la calle Guadalupe, esta cuenta con capacidad de 5 locales\n"
              "tiene una azotea verde y un amplio jardin, hace poco agregaron tres niveles los cuales serian departamentos en venta."
              "\nLas personas que rentan los locales compraron departamento \na 20% de descuento y hubo dos ventas (tu y alguien más)")
        print("\nTranscurrio alrededor de una semana y por la madrugada se escucho una ambulancia que recogio a alguien \n"
              "cercas de aqui.\n\nAlrededor de medio día sales de la plaza y te enteras de los vecinos que {}".format(Nei[random.randint(0,2)]))
        print("tu vecino a sido recogido por la ambulancia, al parecer se encontro \n{}\n".format(Fatal[random.randint(0,2)]))
        print("Recuerdas que escuchaste ruidos por la madrugada, los dueños de los locales parece que no se dieron\n"
              "cuenta, pero estas seguro que pudo haber sido alguno de ellos ya que la plaza se cierra a las 12pm y no hay forma\n"
              "de ingresar a menos que tengas llaves o abrá la plaza a las 7am.\n")
        print("Evitas comentar lo sucedido y decides realizar una investigación, la comisaría mencionó que no vendrán a menos que\n"
              "tengas a alguien en mente y pruebas que entregar. Sales con tu cuaderno y prestas atención a tu alrededor.\n")
        input("Presione enter para continuar . . .\n ")

        pase = Game()

        print("Empieza la búsqueda: \n")
        print("Te das cuenta que muchas áreas fueron limpiadas pero estas seguro que puedes encontrar indicios.\n"
              "Tras lo sucedido ese día los locales no abrieron, entonces puedes interrogar en los departamentos\n")
        print("Recuerda que no te puedes confiar de todo lo que te dicen, quien fuera el culpable va a ocultar sus acciones\n")

        while True:
            print("Puedes realizar algunas de las acciones")
            for x in range(0, len(Menu)):
                if x+1 in Men:
                    print("{}".format(Menu[x]))
            print("Selección una opción: ")
            while True:
                E1 = input()[0:1]
                if E1 != '' and E1.isdigit():
                    if (int(E1) in Men) == False:
                        print("Escribe el número de la opción disponible: ")
                    else:
                        E1 = int(E1)
                        break
                else:
                    print("Escribe el número de la opción disponible: ")

            if E1 == 1:
                if per == []:
                    print("Ya has interrogado a todos, dudo que quieran volver a abrirte\n")
                    input("Presione enter para continuar....")
                else:
                    print("¿A quien vas a interrogar?")
                    for a in range(0, len(person)):
                        if a in per:
                            print('{}) {}'.format(a + 1, person[a]))
                    print("Selección una opción: ")
                    while True:
                        E2 = input()[0:1]
                        if E2 != '':
                            if (int(E2) - 1 in per) == False:
                                print("Escribe el número de la opción disponible: ")
                            else:
                                E2 = int(E2)
                                break
                        else:
                            print("Escribe el número de la opción disponible: ")

                    nom = person[E2 - 1]

                    if pase == nom:
                        print("Lo que sabes de {} es que {}\nTendras que resolver la situacion sin su información\n".format(nom, Intro[E2 - 1]))
                        input("Presione enter para continuar....")
                    else:
                        print("Lo que sabes de {} es que {} en cuanto tocaste el timbre\n".format(nom, Intro[E2 - 1]))
                        input("Presione enter para continuar....")
                        if E2 - 1 <= 1:
                            print("\nTu: Buenas tardes\n{}: {}".format(nom, Get2[E2 - 1]))
                            print("Tu: Una disculpa, pero ¿puede contarme como estuvo su día de ayer?, en especial durante noche")
                            print("{}: {}".format(nom, mood[E2 - 1]))
                            print("\nDurante la conversacion echaste un vistazo al interior del departamento \n{}".format(Look[E2-1]))
                            print("Tu: Gracias\nTe cierra la puerta en la cara\n")
                            input("Presione enter para continuar....")
                        else:
                            print("\n{}: {}".format(nom, Get1[E2 - 1]))
                            print("Tu: Buenas, lamento molestar, ¿puede contarme acerca de su día ayer?, y ¿si escucho algo durante la noche?")
                            print("{}: {}".format(nom, mood[E2 - 1]))
                            print("\nDurante la conversacion echaste un vistazo al interior del departamento \n{}".format(Look[E2 - 1]))
                            print("Tu: Gracias\nTe retiras lo más pronto posible\n")
                            input("Presione enter para continuar....")

                    per.remove(E2-1)

                    if len(per) == 0:
                        Men.remove(1)

            if E1 == 2:
                if len(lug) == 1:
                    print("No tienes todo el día, no puedes perder el tiempo dando una doble vuelta\n")
                    input("Presione enter para continuar....")
                else:
                    print("¿Donde vas a inspeccionar?")
                    for a in range(0, len(place)):
                        if a in lug:
                            print('{}) {}'.format(a + 1, place[a]))
                    print("Selección una opción: ")
                    while True:
                        E2 = input()[0:1]
                        if E2 != '':
                            if (int(E2) - 1 in lug) == False:
                                print("Escribe el número de la opción disponible: ")
                            else:
                                E2 = int(E2)
                                break
                        else:
                            print("Escribe el número de la opción disponible: ")

                    nom = place[E2 - 1]

                    print("Visitas {}, {}\n".format(nom, Des[E2 - 1]))
                    input("Presione enter para continuar....")

                    lug.remove(E2 - 1)



                    if len(lug) == 1:
                        print("Consideras que no es necesario revisar {} porque ya te puedes dar una idea de la situción")
                        Men.remove(2)

            if E1 == 3:
                print("Estas a punto de dar el veredicto. ¿Deseas continuar?")
                print("1. Si\n2. No")
                print("Selección una opción: ")
                while True:
                    E2 = input()[0:1]
                    if (E2 in ['1', '2']) == False:
                        print("Escribe el número de la opción disponible: ")
                    else:
                        break

                if E2 == '1':
                    print("Has llamada a la comisaría y estan prestando atención a tus palabras. Comienzan a interrogarte\n")
                    print("¿Donde fue el atraco de la victima?")
                    for a in range(5):
                        print('{}) {}'.format(a + 1, place[a]))
                    print("Seleccione una opción disponible: ")
                    while True:
                        E3 = input()[0:1]
                        if (E3 in ['1', '2', '3', '4', '5']) == False:
                            print("Escribe el número de la opción disponible: ")
                        else:
                            break
                    Register[1] = place[int(E3) - 1]
                    print("\n¿Sabes con que objeto o arma fue violentado?")
                    for a in range(5):
                        print('{}) {}'.format(a + 1, Weapon[a]))
                    print("Seleccione una opción disponible: ")
                    while True:
                        E3 = input()[0:1]
                        if (E3 in ['1', '2', '3', '4', '5']) == False:
                            print("Escribe el número de la opción disponible: ")
                        else:
                            break
                    Register[2] = Weapon[int(E3) - 1]

                    print("\n¿Quién crees que lo realizo?")
                    for a in range(5):
                        print('{}) {}'.format(a + 1, person[a]))
                    print("Seleccione una opción disponible: ")
                    while True:
                        E3 = input()[0:1]
                        if (E3 in ['1', '2', '3', '4', '5']) == False:
                            print("No existe la opción")
                        else:
                            break
                    Register[0] = person[int(E3) - 1]

                    print("Inmediatamete se digieron con {} y la persona fue detenida sin darle explicación. Van al {}\n"
                          "para echarle un vistazo y toman el {} para muestras".format(Register[0], Register[1], Register[2]))

                    if Register[:] == Killer[:]:
                        print("\nDespués de 12 horas de detención y mostrar la evidencia, se confirma que {} fue culpable.\n"
                              "todos se sienten más tranquilos y los dias han sido cómodos, te sientes seguro esta vez.".format(Register[0]))
                        print("\n****************** ¡Has trabajado mucho, felicidades! *****************\n")
                        input("Presione enter para regresar al menú ....")
                        break
                    else:
                        print("\nAl mostrar la evidencia interrogan e investigan el departamento, pero no es suficiente\n"
                              "para detener a {}, ya que no con esto no se puede imaginar la escena del crimen, entonces se\n"
                              "liberá la persona, tuviste que ofrecer una disculpa y dudas que tu palabra vuelva a ser\n"
                              "creíble, descansas esa noche encerrandote bien y buscando otra ubicación.".format(Register[0]))
                        print("\n******************* ¡Has fracasado en tu intento de detective! **************************\n")
                        input("Presione enter para regresar al menú....")
                        break

            if E1 == 4:
                print("¿Estás seguro de que seas renunciar?")
                print("1. No\n2. Si")
                print("Selección una opción: ")
                while True:
                    E2 = input()[0:1]
                    if (E2 in ['1', '2']) == False:
                        print("Escribe el número de la opción: ")
                    else:
                        break

                if E2 == '2':
                    print("En vez de arriesgarte has decidido renunciar, dejas la situación en manos de alguien más y \n"
                          "buscas otro lugar al cual mudarte con miedo saber cuantas noches puedes vivir antes de encontrar\n"
                          "nuevo departamento.\n\n ******** ¡Suerte y espero puedas sobrevivir la noche! ******\n")
                    print("******************* Has fracasado ******************************")
                    input("Presione enter para regresar al menú ....")
                    break
                else :
                    print("Recapacitas y regresas a la jugada\n")

    elif enter == '2':
        print("Bye, Nos vemos pronto")
        input("Presione enter para salir ....")
        break