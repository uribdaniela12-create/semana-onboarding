print("calculadora")
print("menu")
print("1: sumar")
print("2: restar")
print("3: multiplicar")
print("4: dividir")

opcion= int(input("selecciona una opcion: "))

numero1= float(input("introduzca un valor: "))
numero2= float(input("introduzca un valor: "))

if opcion == 1:
    resultado = numero1 + numero2
    print(resultado)
elif opcion == 2:
    resultado = numero1 - numero2
    print(resultado)
elif opcion == 3:
    resultado = numero1 * numero2
    print(resultado)
elif opcion == 4 and (numero2 ==0 or numero1 == 0):
    print("No se puede")

elif opcion ==4 :
    resultado = numero1 / numero2
    print(resultado)
