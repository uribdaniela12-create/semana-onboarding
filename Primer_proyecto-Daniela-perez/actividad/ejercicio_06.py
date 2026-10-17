numero1= int(input("Ingrese el primer número: "))
numero2= int(input("Ingrese el segundo número: "))
operacion= input("Ingrese la operación a realizar (+, -, *, /): ")
if operacion == "+":
    resultado= numero1 + numero2
    print("El resultado de la suma es:", resultado)
elif operacion == "-":
    resultado= numero1 - numero2
    print("El resultado de la resta es:", resultado)
elif operacion == "*":
    resultado= numero1 * numero2
    print("El resultado de la multiplicación es:", resultado)
elif operacion == "/":
    if numero2 != 0:
        resultado= numero1 / numero2
        print("El resultado de la división es:", resultado)
    else:
        print("Error: No se puede dividir entre cero")
else:
    print("Operación no válida. Por favor, ingrese una operación válida (+, -, *, /).") 