nombre= input("Ingrese nombre de usuario: ")
producto= input("Ingresa nombre del producto: ")
Precio= float(input("Ingrsa valor del prodecto: "))
cantidad= int(input("Cantidad: "))
subtotal = cantidad * Precio

if subtotal >= 500000 :
    descuento = subtotal *0.15

elif subtotal >= 200000:
    descuento = subtotal * 0.10
else:
    descuento = 0

total= subtotal - descuento

print( "Cliente", nombre)
print( "producto", producto)
print( "Cantidad", cantidad)
print( "precio unitario", Precio)
print( "subtotal", subtotal)
print( "descuento", descuento)
print( "total a pagar", total)