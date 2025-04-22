# Solicitamos al usuario por consola mediante "input" y usamos flotantes 
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
operador = input("Ingresa el operador (+, -, *, /): ")
# Usamos condicionales para hacer las operaciones segun la eleccion del usuario 
if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    if num2 == 0:
        resultado = "Error: división por cero" # Restriccion de la division 
    else:
        resultado = num1 / num2
else:
    resultado = "Operador no válido" # En caso de que el usuario ingrese un caracter fuera de los establecidos 
print("Resultado:", resultado) # Si el usuario ingresa todo bien, se imprime el resultado de la operacion elegida 
