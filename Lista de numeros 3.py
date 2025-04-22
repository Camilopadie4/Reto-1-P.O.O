def pedir_lista(): # Definimos una funcion para solicitarle numeros al usuario 
    entrada= input("ingrese lista de numeros separados por comas: ") # Solicitamos por consola
    numeros= [int(num.strip()) for num in entrada.split(",")] # Guardamos los numeros enteros en una lista separados por comas 
    return numeros

def num_primo(a): # Definimos una funcion que identifique numeros primos 
    if a < 2:
        print(f"{a} No es un numero primo porque es menor que 2") # Si el algun numero es menor que 2, no es primo 
        return False
    for i in range(2, a): # Iteramos desde 2 hasta la cantidad "a" de numeros
        if a % i== 0:
            print(f"{a} no es primo porque es divisible por {i}.") 
            return False # Si el numero es divisible por otros que no sean 1 y el mismo 
    print(f"{a} es primo porque solo es divisible por 1 y por sí mismo.")  
    return True  # Siempre que se cumpla la condicion fundamental de un numero primo

def filtrar_primos(lista): # Definimos una funcion que extraiga y guarde en una lista los numeros primos. 
    return [num for num in lista if num_primo(num)] # Esta lista guarda los numeros que cumplan la con la definicion de "Num_primo"

Numeros = pedir_lista() # Convocamos la funcion "pedir lista"

print("Numeros primos en la lista", filtrar_primos(Numeros)) # Imprime la lista de numeros primos filtrados por la Fun. "Filtrar-primos"
