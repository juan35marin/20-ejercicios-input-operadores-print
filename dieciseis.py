#  16. Pide al usuario dos números y muestra si ambos son mayores que 10 (usar operador lógico and).

numero1 = int(input("Ingrese numero: "))
numero2 = int(input("Ingrese numero: "))

if numero1 > 10 and numero2 > 10:
    print("Son mayores")
else:
    print("no son mayores")