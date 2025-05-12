# 3. Pide dos números decimales (float) y muestra su multiplicación.

numero1 = float(input("Ingrese numero decimal: "))
numero2 = float(input("Ingrese numero decimal: "))

multiplicacion = numero1 * numero2
print(f"El resultado es: {multiplicacion}")

print(type(multiplicacion).__name__)
