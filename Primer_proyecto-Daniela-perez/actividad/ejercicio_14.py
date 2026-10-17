saldo = 500000

while True:
 print("CAJERO")
 print("1 : consultar saldo")
 print("2 : retirar dinero ")
 print("3 : depositar dinero")
 print("4 : salir ")

 opcion= int(input("elija una opcion: " ))

 if opcion == 1: 
  print("saldo actual es :", saldo)
 elif opcion == 2:
  retiro= float(input("¿cuanto dinero deseas retirar?: "))
  if retiro <= 0:
    print("El valor debe ser mayor a cero")
  elif retiro > saldo:
    print("saldo insuficiente ")
  else:
    saldo= saldo - retiro
    print("saldo", saldo)
 elif opcion == 3:
  deposito = float(input("¿ cuanto dinero desear depositar?:"))
  if deposito <0:
   print("El valor debe ser mayor a cero")
  else:
   saldo = deposito + saldo
   print("Saldo:", saldo)
 elif opcion == 4:
  print("Gracias por utiliar nuestro servivio")
  break


  