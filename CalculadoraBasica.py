""""
La idea es crear una calculadora básica que pueda realizar operaciones como suma, resta, multiplicación y división.
El programa solicitará al usuario que ingrese dos números y la operación que desea realizar, 
luego mostrará el resultado de la operación.
y se ejecutara en un loopp while para permitir al usuario realizar múltiples cálculos hasta que decida salir.
"""
indicacion = ""
while indicacion.lower() != "salir":
    indicacion = input("Ingrese la operación que desea realizar (Suma, Resta, Multiplicacion, Division) o 'Salir' para terminar: ")
    if indicacion.lower() == "salir":
        print("Gracias por usar la calculadora. ¡Hasta luego!")
        break
    elif indicacion.lower() == "suma":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 + num2
        print(f"El resultado de la suma es: {resultado}")
    elif indicacion.lower() == "resta":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 - num2
        print(f"El resultado de la resta es: {resultado}")  
    elif indicacion.lower() == "multiplicacion":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 * num2
        print(f"El resultado de la multiplicación es: {resultado}")
    elif indicacion.lower() == "division":  
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        if num2 != 0:
            resultado = num1 / num2
            print(f"El resultado de la división es: {resultado}")
        else:
            print("Error: No se puede dividir por cero.")
            break
    else:
        print("Operación no válida. Por favor, intente nuevamente.")
    
    
    