#################### Paquetes Utilizados En La Creacion Del Script ###################
#2to3

#################### Importando Librerias Para Compilar ###################
######## Quitar El # Para Descomentar #########
import sys
#import os
#import math
#import tkinter

################# Opciones De Inicio ######################
print("Menu")
print("Bienvenido A La Multi-Calculadora De Python")
print("Para Salir Del Programa Presione 0")
print("Para Correr El Programa Presione 1")
raw_input = input(": ")
if raw_input == ("0"):
    sys.exit()
if raw_input == ("1"):
    ...

################ Opciones De Arranque #######################
print("Menu")
print("Presione 1 Para Iniciar Diferenciador")
print("Presione 2 Para Iniciar Calculadora")
print("Presione 3 Para Iniciar Calculos Fisicos")
raw_input = input(": ")
if raw_input == ("1"):
    print("Bienvenido Al Comparador De Numeros En Python")
    print("Para Salir Del Programa Escriba Quit")
    print("Para Comenzar Escriba Start")
    raw_input = input(": ")
    if raw_input == ("Quit"):
        sys.exit()
    if raw_input == ("Start"):
        ...
############# Diferenciar Numeros Comandos #####################
    num1 = (input("Enter a number: "))
    num2 = (input("Enter another number: "))
    ############# Si Los Digitos Ingresados Son Iguales #######################
    if num1 == num2:
        result = num1 == num2
        print("El Numero " + str(num1) + " " + "Es Igual A" + " " + str(num2))
        sys.exit()
########### Si Los Digito Ingresado Es Menor que NUM1 Que NUM2 ###################
    elif num1 < num2:
        result = num1 < num2
        print("El Numero " + str(num1) + " " + "Es Menor A" + " " + str(num2))
        sys.exit()
############# Si Los Digito Ingresado Es Mayor NUM1 Que NUM2 ###################
    else:
        num1 > num2
        result = num1 > num2
        print("El Numero " + str(num1) + " " + "Es Mayor A" + " " + str(num2))
        sys.exit()
#################### Calculadora Comandos ####################
elif raw_input == ("2"):
    ...

    #################### Estructura De Operandos ###################
    def calculadora(numero1, numero2):
        #################### Estructura De Operandos Suma ###################
        if opcion == 'a':
            resultado = numero1 + numero2
            operacion = ' + '
#################### Estructura De Operandos Resta ###################
        if opcion == 'b':
            resultado = numero1 - numero2
            operacion = ' - '
#################### Estructura De Operandos Multiplicacion ###################
        if opcion == 'c':
            resultado = numero1 * numero2
            operacion = ' * '
#################### Estructura De Operandos Division ###################
        if opcion == 'd':
            if numero2 != 0:
                resultado = numero1 / numero2
                operacion = ' / '
            else:
                print("ERROR: no se puede dividir por 0")
        final1 = str(numero1) + operacion + str(numero2) + ' = ' + str(
            resultado)
        return final1

#################### Estructura De Menus ###################

    print('''
    ///CALCULADORA///
    Que operacion desea hacer?
    a) Sumar
    b) Restar
    c) Multiplicar
    d) Dividir
    e) Salir''')

    opcion = input('Elija una opcion: ')
    if opcion != 'a' and opcion != 'b' and opcion != 'c' and opcion != 'd' and opcion != 'e':
        print('ERROR: Opcion introducida no se reconoce.')
        input('Pulse para continuar intro....')
#################### Rompiendo El Bucle/Loop a###################
    else:
        if opcion == 'e':
            sys.exit()
#################### Reintento De calculo De Datos ###################
        try:
            numero1 = float(input('Introduce un numero: '))
            numero2 = float(input('Introduce otro numero: '))
            print(calculadora(numero1, numero2))
            input('Pulse para continuar intro....')
#################### Excepciones a###################
        except:
            print('ERROR: los numeros introducidos no se pueden procesar.')
            input('Pulse para continuar intro....')
######################### END  OF PROGRAMA ###################################

######################### Estructura Calculadora Cientifica Multi-Funcion #########################
if raw_input == ("3"):
    print("¡Bienvenido Al Calculador De Operaciones Fisicas!")
    print("Por Favor Seleccione El Tema De Su Interes")
    print("A. Cinematica/Movimientos")
    print("B. Energias")
    print("C. Elasticidad")
    print("D. Equilibrio Termico")
    print("E. Leyes Fisicas")
    print("F. Gravedad")
    raw_input = input(": ")

    ############# Constitucion Del Menu Fisico I. Cinematica #########################
    if raw_input == ("A"):
        ...
        print("Menu")
        print("A. Movimiento Uniforme Rectilineo")
        print("B. Movimiento Uniformemente Acelerado")
        print("C. Movimiento Circular Uniforme")
        print("D. Movimiento Armonico Simple")
        print("E. Movimiento Parabolico")
    raw_input = input(": ")

    ############# Constitucion Del Menu Fisico I. Movimiento Uniforme Rectilineo #####################
    if raw_input == ("A"):
        print("Menu")
        print("A. ¿Que Es?")
        print("B. Ecuaciones")
        print("C. ¿Que Implica Que Sea Un Movimiento Rectilineo?")
        print("D. ¿Que Unidades Intervienen En Este Movimiento?")
        print("E. Bibligorafias")
        raw_input = input(": ")

        ############# I° Operacion; I° Sub-Conjunto Pregunta A ###################
        if raw_input == ("A"):
            ...
            print(
                " Usted Se Encuentra En: Que Es Un Movimiento Uniformente Rectilineo"
            )
            " "
            print(
                "El movimiento rectilíneo uniforme (m.r.u.), es aquel con velocidad constante y cuya trayectoria es una línea recta. Un ejemplo claro son las puertas correderas de un ascensor, generalmente se abren y cierran en línea recta y siempre a la misma velocidad."
            )

            sys.exit()

############# I° Operacion; I° Sub-Conjunto Pregunta B ###################
        if raw_input == ("B"):
            ...
            print(
                "Usted Se Encuentra En: Ecuaciones De Movimiento Uniforme Rectilineo"
            )
            " "
            print("POSICION")
            " "
            print(
                "Módulo vector posición en coordenadas cartesianas en 2 dimensiones"
            )
            print("r=√x2+y2")
            " "
            print("DESPLAZAMIENTO Y ESPACIO RECORRIDO")
            " "
            print(
                "Módulo del vector desplazamiento en dos dimensiones en cartesianas "
            )
            print("r=√(xf−xi)2+(yf−yi)2")
            " "
            print("CELERIDAD O RAPIDEZ")
            " "
            print("Celeridad O Rapidez Media")
            print("cm = Δs/Δt= s2−s1/t2 − t1")
            " "
            print("VELOCIDAD")
            " "
            print("Modulo Velocidad")
            print("v=Δr/Δt")
            " "
            print("ACELERACION")
            " "
            print("Modulo Aceleracion")
            print("a=Δv/Δt=vf−vi/tf−ti")
            " "
            sys.exit()

############# I° Operacion; I° Sub-Conjunto Pregunta C ###################
        if raw_input == ("C"):
            ...
            print("El espacio recorrido es igual que el desplazamiento.")
            print("En tiempos iguales se recorren distancias iguales.")
            print(
                "La rapidez o celeridad es siempre constante y coincide con el módulo de la velocidad."
            )

            sys.exit()

################ I° Operacion; I° Sub-Conjunto Pregunta D ###################
        if raw_input == ("D"):
            ...
            print("Velocidad -> v")
            print("Masa -> m")
            print("Tiempo -> t")

            sys.exit()

################ I° Operacion; I° Sub-Conjunto Pregunta E ###################
        if raw_input == ("D"):
            ...
            print("BIBLIOGRAFIAS")
            print("https://www.fisicalab.com/apartado/mru")
            sys.exit()

############# Constitucion Del Menu Fisico I. Movimiento Uniforme Acelerado #####################
    if raw_input == ("B"):
        print("Menu")
        print("A. ¿Que Es?")
        print("B. Ecuaciones")
        print("C. ¿Que Implica Que Sea Un Movimiento Acelerado?")
        print("D. ¿Que Unidades Intervienen En Este Movimiento?")
        print("E. Bibligorafias")
        raw_input = input(": ")

        ################# I° Operacion; II° Sub-Conjunto Pregunta A ###################
        if raw_input == ("A"):
            ...
            print(
                " Usted Se Encuentra En: Que Es Un Movimiento Uniformente Acelerado "
            )
            " "
            print(
                "Es aquel movimiento en el que la aceleración que experimenta un cuerpo, permanece constante (en magnitud vectores y dirección) en el transcurso del tiempo manteniéndose firme."
            )

            sys.exit()

############# I° Operacion; II° Sub-Conjunto Pregunta B ###################
        if raw_input == ("B"):
            ...
            print(
                "Usted Se Encuentra En: Ecuaciones De Movimiento Uniforme Acelerado"
            )
            " "
            print("VELOCIDAD")
            " "
            print(
                "Hallar La Velocidad De Un Objeto, Dependiendo Tanto Del Tiempo,Aceleracion"
            )
            print("v=vi+a⋅t")
            print("v2=vi2+2⋅a⋅Δx")
            " "
            print("POSICION")
            " "
            print(
                " Hallar La Posicion De Un Cuerpo En Un Determinado Espacio, Teniendo En Cuenta Su Acelearcion, Velocidad Y El Tiempo "
            )
            print("x=xi+vi*t+1/2*a*t2")
            " "
            print("TIEMPO")
            " "
            print(
                "Hallamos El Tiempo A Partir De La Velocidad Final Y La Inicial Y La Aceleracion"
            )
            " "
            print("t=vf−vi/a")
            " "
            sys.exit()

############# I° Operacion; II° Sub-Conjunto Pregunta C ###################

        if raw_input == ("C"):
            ...
            print(
                "La trayectoria es una línea recta y por tanto, la aceleración normal es cero; la velocidad instantánea cambia su módulo de manera uniforme aumenta o disminuye en la misma cantidad por cada unidad de tiempo. Esto implica el siguiente punto; la aceleración tangencial es constante. Por ello la aceleración media coincide con la aceleración instantánea para cualquier periodo estudiado a=am"
            )

            sys.exit()

################ I° Operacion; II° Sub-Conjunto Pregunta D ###################

        if raw_input == ("D"):
            ...
            print("Velocidad Inicial -> Vi")
            print("Velocidad Final -> Vf")
            print("Tiempo -> t")
            print("Aceleracion -> a")
            print("Posicion -> x")

            sys.exit()

################ I° Operacion; II° Sub-Conjunto Pregunta E ###################

        if raw_input == ("D"):
            ...
            print("BIBLIOGRAFIAS")
            print("https://www.fisicalab.com/apartado/mrua-ecuaciones")

            sys.exit()

        ############# I° Operacion; III° Sub-Conjunto Pregunta A ###################
        if raw_input == ("A"):
            ...
            print(
                " Usted Se Encuentra En: Que Es Un Movimiento Circular Unifome"
            )
            " "
            print(
                "El movimiento rectilíneo uniforme (m.r.u.), es aquel con velocidad constante y cuya trayectoria es una línea recta. Un ejemplo claro son las puertas correderas de un ascensor, generalmente se abren y cierran en línea recta y siempre a la misma velocidad."
            )

            sys.exit()

############# I° Operacion; III° Sub-Conjunto Pregunta B ###################
        if raw_input == ("B"):
            ...
            print(
                "Usted Se Encuentra En: Ecuaciones De Movimiento Uniforme Rectilineo"
            )
            " "
            print("POSICION")
            " "
            print(
                "Módulo vector posición en coordenadas cartesianas en 2 dimensiones"
            )
            print("r=√x2+y2")
            " "
            print("DESPLAZAMIENTO Y ESPACIO RECORRIDO")
            " "
            print(
                "Módulo del vector desplazamiento en dos dimensiones en cartesianas "
            )
            print("r=√(xf−xi)2+(yf−yi)2")
            " "
            print("CELERIDAD O RAPIDEZ")
            " "
            print("Celeridad O Rapidez Media")
            print("cm = Δs/Δt= s2−s1/t2 − t1")
            " "
            print("VELOCIDAD")
            " "
            print("Modulo Velocidad")
            print("v=Δr/Δt")
            " "
            print("ACELERACION")
            " "
            print("Modulo Aceleracion")
            print("a=Δv/Δt=vf−vi/tf−ti")
            " "
            sys.exit()

############# I° Operacion; III° Sub-Conjunto Pregunta C ###################
        if raw_input == ("C"):
            ...
            print("El espacio recorrido es igual que el desplazamiento.")
            print("En tiempos iguales se recorren distancias iguales.")
            print(
                "La rapidez o celeridad es siempre constante y coincide con el módulo de la velocidad."
            )

            sys.exit()

################ I° Operacion; III° Sub-Conjunto Pregunta D ###################
        if raw_input == ("D"):
            ...
            print("Velocidad -> v")
            print("Masa -> m")
            print("Tiempo -> t")

            sys.exit()

################ I° Operacion; III° Sub-Conjunto Pregunta E ###################
        if raw_input == ("D"):
            ...
            print("BIBLIOGRAFIAS")
            print("https://www.fisicalab.com/apartado/mru")
            sys.exit()

############# Constitucion Del Menu Fisico II. Energias ###################
    if raw_input == ("B"):
        ...
        print("Menu")
        print("A. Energia Cinetica")
        print("B. Energia Potencial")
        print("C. Energia Potencial Gravitatoria")
        print("D. Energia Potencial Elastica")
        print("E. Energia Quimica")
        print("F. Energia Termica")
    raw_input = input(": ")

    ############# Constitucion Del Menu Fisico III. Elasticidad ###################
    if raw_input == ("C"):
        ...
    raw_input = input(": ")

    ############# Constitucion Del Menu Fisico IV. Equilibrio Termico ###################
    if raw_input == ("D"):
        ...
    raw_input = input(": ")

    ############# Constitucion Del Menu Fisico V. Leyes Fisicas ###################
    if raw_input == ("E"):
        ...
    raw_input = input(": ")

    ############# Constitucion Del Menu Fisico VI. Gravedad ###################
    if raw_input == ("F"):
        ...
        print("A. Caida Libre")
        print("B. Tiro Vertical")
    raw_input = input(": ")
