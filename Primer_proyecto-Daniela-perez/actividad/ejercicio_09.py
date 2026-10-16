precio = float(input("Ingrese el precio del producto: "))
if precio >= 200.000:
    descuento = precio * 0.20
    print("El descuento es de:", descuento)
    precio_final = precio - descuento
    print("El precio final es:", precio_final)
elif precio >= 100.000:
    descuento = precio * 0.10
    print("El descuento es de:", descuento)
    precio_final = precio - descuento
    print("El precio final es:", precio_final)
else:
    print("No hay descuento para este producto")
    print("El precio final es:", precio)
    