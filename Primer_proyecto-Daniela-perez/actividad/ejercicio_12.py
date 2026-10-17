lado1 = float(input("escribe la medida del lado a: "))
lado2 = float(input("escribe la medida del lado b: "))
lado3 = float(input("escribe la medida del lado c: "))
if lado1 == lado2 and lado2 == lado3 :
    print("El triangulo es equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("El tiengulo es isóceles ")
else:
    print("El triangulo es escaleno")
