numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
suma = numero1 + numero2
resta = numero1 - numero2

print("La suma de", numero1, "y", numero2, "es:", suma)
print("La resta de", numero1, "y", numero2, "es:", resta)
if suma > 10:
    print("La suma es mayor que 10")
else:
    print("La suma es menor o igual a 10")

