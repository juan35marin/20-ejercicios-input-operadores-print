# 10. Pide un número entero y muestra el número elevado a la 2 (al cuadrado) y a la 3 (al cubo), usando f-strings.

numero = int(input("ingrese numero entero: "))
cuadrado = str(numero ** 2)
print (type(cuadrado).__name__)
cubo = str(numero ** 3) 
print (type(cubo).__name__)

print (f" el {numero} al cuadrado es {cuadrado} y el cubo {cubo}")
