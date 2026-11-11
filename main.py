numero1 = float(input("Escribir el numero"))
numero2 = float(input("Escribir el numero"))

resultado = numero1 + numero2

print(resultado)

numero1 = float(input("Escribir el numero"))
numero2 = float(input("Escribir el numero"))

resultado = numero2 - numero1

print(resultado)


numero1 = float(input("Escribir el numero"))
numero2 = float(input("Escribir el numero"))

resultado = numero2 * numero1

print(resultado)


numero1 = float(input("Escribir el numero"))
numero2 = float(input("Escribir el numero"))

resultado = numero1 / numero2

print(resultado)

numero1 = float(input("Escribir el numero"))
numero2 = float(input("Escribir el numero"))

resultado = numero1 % numero2

print(resultado)

numero1 = float(input("Escribir el numero"))
numero2 = float(input("Escribir el numero"))

operacion = input("Que operacion deseas utilizar")
if operacion == "+":
    resultado = numero1 + numero2
    print(resultado)

elif operacion == "-":
    resultado = numero1 - numero2
    print(resultado)

elif operacion == "*":
    resultado = numero1 * numero2
    print(resultado)

elif operacion == "/":
    if numero2 == 0:
        print("No se puede dividir entre cero")
        exit()
    resultado = numero1 / numero2
    print(resultado)

else:
    print("Operación no válida")
    exit()

numero1 = float(input("Escribir el numero"))
numero2 = float(input("Escribir el numero"))
numero3 = float(input("Escribir el numero"))
resultado = numero1 + numero2 + numero3
