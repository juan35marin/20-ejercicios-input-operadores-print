# 8. Pide al usuario dos números y muestra la división entera (//) y el módulo (%) entre ellos.

numero1 = int(input("Ingrese numero: "))
numero2 = int(input("Ingrese numero: "))

division_entera = numero1 // numero2
print(f"La division entera fue igual a: {division_entera}")
modulo = numero1 % numero2
print(f"El modulo es igual a: {modulo}")
