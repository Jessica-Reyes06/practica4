from funciones_aritemticas import *
from funciones_geometricas import *
from fun_trigo import *
from conversiones import *


while True:
    print("Seleccione una opción:")
    print("1. Funciones Aritméticas")
    print("2. Funciones Geométricas")
    print("3. Funciones Trigonométricas")
    print("4. Conversiones")
    print("5. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    match opcion:
        case "1":
            print ("Opciones de Funciones Aritméticas:")
            print("1. Suma")
            print("2. Resta")
            print("3. Multiplicación")
            print("4. División")

            op = input("Ingrese el número de la operación deseada: ")
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))

            match op:
                case "1":
                    print(f"Resultado: {sumar(a, b)}")
                case "2":
                    print(f"Resultado: {restar(a, b)}")
                case "3":
                    print(f"Resultado: {multiplicar(a, b)}")
                case "4":
                    try:
                        print(f"Resultado: {dividir(a, b)}")
                    except ValueError as e:
                        print(e)
        case "2":
            print ("Opciones de Funciones Geométricas:")
            print("1. Área de un círculo")
            print("2. Área de un rectángulo")
            print("3. Área de un triángulo")
            print("4. Área de un cuadrado")
            op = input("Ingrese el número de la operación deseada: ")
            match op:
                case "1":
                    radio = float(input("Ingrese el radio del círculo: "))
                    print(f"Área del círculo: {area_circulo(radio)}")
                case "2":
                    base = float(input("Ingrese la base del rectángulo: "))
                    altura = float(input("Ingrese la altura del rectángulo: "))
                    print(f"Área del rectángulo: {area_rectangulo(base, altura)}")
                case "3":
                    base = float(input("Ingrese la base del triángulo: "))
                    altura = float(input("Ingrese la altura del triángulo: "))
                    print(f"Área del triángulo: {area_triangulo(base, altura)}")
                case "4":
                    lado = float(input("Ingrese el lado del cuadrado: "))
                    print(f"Área del cuadrado: {area_cuadrado(lado)}")
        case "3":
            print ("Opciones de Funciones Trigonométricas:")
            print("1. Seno")
            print("2. Coseno")
            print("3. Tangente")
            op = input("Ingrese el número de la operación deseada: ")
            angulo = float(input("Ingrese el ángulo en grados: "))
            match op:
                case "1":
                    print(f"Seno de {angulo} grados: {sin(angulo)}")
                case "2":
                    print(f"Coseno de {angulo} grados: {cos(angulo)}")
                case "3":
                    print(f"Tangente de {angulo} grados: {tan(angulo)}")
        case "4":
            print ("Opciones de Conversiones:")
            print ("1. Celsius a Farenheit")
            print ("2. Farenheit a Celsius")
            print ("3. Kilómetros a Millas")
            print ("4. Millas a Kilómetros")
            print ("5. Kilogramos a Libras")
            print ("6. Libras a Kilogramos")
            op = input("Ingrese el número de la operación deseada: ")
            valor = float(input("Ingrese el valor a convertir: "))
            match op:
                case "1":
                    print(f"{valor} grados Celsius son {celsius_a_farenheit(valor)} grados Farenheit")
                case "2":
                    print(f"{valor} grados Farenheit son {farenheit_a_celsius(valor)} grados Celsius")
                case "3":
                    print(f"{valor} kilómetros son {kilometros_a_millas(valor)} millas")
                case "4":
                    print(f"{valor} millas son {millas_a_kilometros(valor)} kilómetros")
                case "5":
                    print(f"{valor} kilogramos son {kilogramos_a_libras(valor)} libras")
                case "6":
                    print(f"{valor} libras son {libras_a_kilogramos(valor)} kilogramos")
        case "5":
            print("Saliendo del programa...")
            break
        case _:
            print("Opción no válida. Por favor, intente nuevamente.")